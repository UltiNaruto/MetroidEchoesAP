# Generation Fix Notes

This document explains in detail what was broken, why it was broken, and how each
fix works. Intended as a reference for code review.

---

## Background: How Archipelago fills locations

Archipelago's generation runs in roughly this order:

1. **`fill_restrictive`** — Places progression items one at a time, always checking
   that the item being placed is reachable from the current state, and that the game
   remains beatable after placement.

2. **`accessibility_corrections`** — After progression is placed, runs a BFS sweep
   starting from only the precollected items (no collected items yet). Sweeps items
   from accessible locations into state, then re-checks what new locations open up,
   and repeats until nothing new is reachable. Any location that is NEVER reached
   during this sweep is flagged as permanently inaccessible.

3. **`remaining_fill`** — Tries to place remaining filler items (Missile Expansions,
   Beam Ammo Expansions, etc.) into remaining unfilled locations. If any location is
   inaccessible and there are still items to place, this throws:
   `FillError: No more spots to place N items`.

4. **Final beatability check** — After all items are placed, checks whether the
   game's completion condition can be satisfied. If not, throws:
   `FillError: Game appears as unbeatable`.

### Note on `can_access` and event items

`MetroidPrime2Location.__init__` accepts a `can_access` parameter but does **not**
call `set_rule` with it, so location-level access rules are never enforced by
Archipelago. This means:
- All event locations (locked items) are always swept when their **region** is
  accessible, regardless of what their `can_access` lambda says.
- Pickup locations are also always accessible once their region is reachable —
  `fill_restrictive` and the accessibility sweep don't check `can_access`.

### Note on `DoorCover.Opened` and the tuple bug

In `logic/__init__.py`, `_set_rule` has a trailing comma bug:

```python
def _set_rule(entrance, exit_, player):
    def exit_rule(state):
        condition = exit_.rule(state, player),  # ← trailing comma makes a tuple!
        if exit_.door != DoorCover.Opened:
            condition = condition_and([...])
        return condition  # for Opened doors: returns (True,) or (False,) — always truthy!
    set_rule(entrance, lambda state: exit_rule(state))
```

For `DoorCover.Opened` exits, `condition` is never updated after the first line, so
it returns a 1-element tuple. In Python, any non-empty tuple is truthy, so **all
`DoorCover.Opened` exits are always passable regardless of their rule lambda**. This
bug is not fixed in this PR (it would require careful review of every Opened exit's
intended gating), but it's important to know about when reading the fix logic.

---

## Fix 1 — GFMC Compound (Above Ship): missing inbound connection

**File:** `src/logic/metroidprime2/light_world/temple_grounds/gfmc_compound.py`

### What was wrong

The room has multiple sub-regions including `GFMCCompound_Center` and
`GFMCCompound_AboveShip`. The Above Ship sub-region contained the second Missile
Expansion pickup and had one exit: back to Center. But Center had no exit going the
other direction — into Above Ship. The region was a complete dead end with no way in.

`accessibility_corrections` could never sweep the Above Ship region because no
entrance connected to it, so its pickup was permanently inaccessible.

### The fix

Added a `MetroidPrime2Exit` from `GFMCCompound_Center.exits_` to
`"Temple Grounds - GFMC Compound (Above Ship)"`:

```python
MetroidPrime2Exit(
    destination="Temple Grounds - GFMC Compound (Above Ship)",
    door=DoorCover.Opened,
    rule=lambda state, player: state.has_all({
        "Temple Grounds - GFMC Compound | Cannon Activated",
        "Morph Ball",
    }, player),
),
```

In practice this is always passable from base state because:
- Morph Ball is precollected
- Cannon Activated is an event in GFMC Center with `can_access` = Scan Visor
  (precollected), and since `can_access` is not enforced, it's swept immediately
  when Center is accessible
- And even if the rule were checked, `DoorCover.Opened` + tuple bug = always truthy

---

## Fix 2 — Completion condition: wrong item name

**File:** `src/logic/__init__.py`

### What was wrong

```python
multiworld.completion_condition[player] = lambda state: state.has("Victory", player)
```

The Victory event item is defined in `sky_temple_gateway.py` as:

```python
MetroidPrime2Item(
    name="Sky Temple Grounds - Sky Temple Gateway | Victory",
    ...
)
```

`state.has("Victory", player)` checks for an item literally named `"Victory"`. No
such item exists in the game — the item is named with the full region path following
the convention used by all other event items in this codebase. So the condition
always returned False, making every generated game appear unbeatable.

### The fix

```python
multiworld.completion_condition[player] = lambda state: state.has(
    "Sky Temple Grounds - Sky Temple Gateway | Victory", player
)
```

---

## Fix 3 — `set_rules`: credits exits connect to wrong region

**File:** `src/logic/__init__.py`

### What was wrong

In the `disabled` and `emperor_ing_only` final boss modes, `set_rules` creates an
extra exit to the Credits region:

```python
exit_to_credits = sky_temple_gateway.create_exit(...)
exit_to_credits.connect(sky_temple_gateway)  # ← bug: should be credits_outro
```

`exit_to_credits.connect(sky_temple_gateway)` connects the exit back to the region
it came from — a self-loop that does nothing. The `credits_outro` region was never
actually connected. This didn't affect the default (`all` bosses) mode, but would
cause issues for those two options.

### The fix

```python
exit_to_credits.connect(credits_outro)  # both occurrences
```

---

## Summary table

| # | File | Bug | Impact |
|---|------|-----|--------|
| 1 | `gfmc_compound.py` | Above Ship sub-region unreachable (no inbound exit) | 1 location permanently inaccessible |
| 2 | `logic/__init__.py` | Completion condition checks wrong item name (`"Victory"` vs full path) | Game always appears unbeatable |
| 3 | `logic/__init__.py` | Credits exits self-loop instead of connecting to credits region | Affects `disabled`/`emperor_ing_only` final boss modes |
