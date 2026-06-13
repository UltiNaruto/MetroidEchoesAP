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

The key thing about `accessibility_corrections` is that it starts from scratch with
only precollected items. This means if a progression item is placed behind a door
that requires another progression item, and neither item can be reached from base
state, you get a deadlock. The 15 inaccessible locations in this PR were all
deadlocked in exactly this way — the rooms were physically connected in the graph
but their entry conditions required items that were themselves unreachable.

### Note on `can_access` and event items

`MetroidPrime2Location.__init__` accepts a `can_access` parameter but does **not**
call `set_rule` with it, so location-level access rules are never enforced by
Archipelago. This means:
- All event locations (locked items) are always swept when their **region** is
  accessible, regardless of what their `can_access` lambda says.
- Pickup locations are also always accessible once their region is reachable —
  `fill_restrictive` and the accessibility sweep don't check `can_access`.

This is important for understanding several of the fixes below.

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
is why portal traversal (which uses `DoorCover.Opened`) works freely, and why
sub-region transitions (also `DoorCover.Opened`) are always traversable. This bug is
not fixed in this PR (it would require careful review of every Opened exit's
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

## Fix 2 — Hydrodynamo Station: no trick-free path to Hydrodynamo Shaft

**File:** `src/logic/metroidprime2/light_world/torvus_bog/hydrodynamo_station.py`

### What was wrong

The exit from Hydrodynamo Station to Hydrodynamo Shaft required:

```python
Space Jump Boots + (
    (Screw Attack + Air Underwater trick)
    OR Underwater Dash trick
)
```

With tricks disabled (the default), both alternatives were False, making Hydrodynamo
Shaft permanently inaccessible. This blocked a large downstream chain:

```
Hydrodynamo Shaft
  → Main Hydrochamber (always passable)
    → portal to Undertemple (DoorCover.Opened → always passable via tuple bug)
      → Undertemple Access (Power Bomb + events + SJB + suit)
        → Undertemple Shaft
          → Crypt Tunnel
            → Crypt
              → portal to Gathering Hall (DoorCover.Opened → always passable)
                → Gathering Hall
                  → Catacombs
                    → Transit Tunnel East
                    → Transit Tunnel South
                    → Dungeon
```

That's 12+ locations blocked by this one missing path.

### The fix

Added `Gravity Boost` as the first alternative in the navigation `condition_or`:

```python
condition_or([
    state.has("Gravity Boost", player),  # ← added
    condition_and([
        can_use_screw_attack(state, player),
        has_trick_enabled(state, player, "Air Underwater"),
    ]),
    has_trick_enabled(state, player, "Underwater Dash"),
]),
```

Gravity Boost is a normal progression item placed in the item pool. Once it's swept
(from wherever `fill_restrictive` placed it), Hydrodynamo Shaft and the entire
downstream chain become accessible.

---

## Fix 3 — Dark Forgotten Bridge: no trick-free path to Dark Arena Tunnel

**File:** `src/logic/metroidprime2/dark_world/dark_torvus_bog/dark_forgotten_bridge.py`

### What was wrong

The exit to Dark Arena Tunnel had a two-part `condition_and`. The second part was:

```python
condition_and([
    state.has("Space Jump Boots", player),
    condition_or([
        condition_and([Morph Ball, bombs, Bomb Space Jump trick, suit]),
        condition_and([Movement trick, Standable Terrain trick, suit]),
    ]),
])
```

With tricks disabled, both branches of the inner `condition_or` were False, making
the entire second part always False. Since it was wrapped in `condition_and` with the
first part, the whole exit rule was always False without tricks.

In the actual game, once you rotate the bridge (an in-room event), you can simply
walk/jump across with Space Jump Boots and suit protection. The rotated bridge event
is placed at a location in Dark Forgotten Bridge — and since `can_access` is not
enforced, it's always in state when the region is accessible.

### The fix

Added the rotated bridge event as the first alternative in the inner `condition_or`:

```python
condition_or([
    condition_and([  # ← added: rotated bridge path
        state.has(
            "Dark Torvus Bog - Dark Forgotten Bridge | Event - Dark Forgotten Bridge Rotated",
            player
        ),
        condition_or([
            has_dark_suit(state, player),
            has_light_suit(state, player),
            state.count("Energy Tank", player) >= 1,
        ]),
    ]),
    condition_and([Morph Ball, bombs, Bomb Space Jump trick, suit]),
    condition_and([Movement trick, Standable Terrain trick, suit]),
])
```

Since the event is always swept when Dark Forgotten Bridge is accessible, this path
is always available with SJB + suit/ETank. Dark Arena Tunnel and Dark Torvus Arena
(2 locations) become reachable.

---

## Fix 4 — Judgment Pit: `condition_and` should be `condition_or` (translator bug)

**File:** `src/logic/metroidprime2/dark_world/dark_agon_wastes/judgment_pit.py`

### What was wrong

The exit to Dark Agon Temple Access had this outer structure:

```python
rule=lambda state, player: condition_and([
    condition_and([
        # normal path: suit + (SJB or Bomb Jump trick or Screw Attack + Standable trick)
        ...
    ]),
    condition_and([
        # trick-only path: Screw Attack without Space Jump trick
        can_use_screw_attack(state, player, z_axis=True),
        has_trick_enabled(state, player, "Screw Attack without Space Jump"),
        not (False),
        condition_or([suit conditions]),
    ]),
])
```

The outer `condition_and` means BOTH paths must be true simultaneously. The second
path requires the "Screw Attack without Space Jump" trick, which is always disabled
by default. So the entire exit rule was always False without that specific trick
enabled — even if the player had Space Jump Boots and a suit, which is all they
actually need.

This appears to be a `rando_translator.py` translation error: the two alternatives
should be joined by `condition_or` (either path works), not `condition_and` (both
paths must work at once).

The same bug appears on the exit to Warrior's Walk in the same room — that one also
has an outer `condition_and` wrapping two alternative paths. However, Warrior's Walk
was already accessible via another route so it wasn't causing a fill error. It may
still be worth reviewing.

### The fix

Changed the outermost `condition_and` to `condition_or` on the Dark Agon Temple
Access exit:

```python
rule=lambda state, player: condition_or([  # ← was condition_and
    condition_and([
        # normal path
        ...
    ]),
    condition_and([
        # trick-only path (Screw Attack without Space Jump)
        ...
    ]),
])
```

This unblocks: Judgment Pit → Dark Agon Temple Access → Dark Agon Temple → Trial
Tunnel (2 locations).

---

## Fix 5 — Completion condition: wrong item name

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

This bug was hidden until Fix 1–4 were applied: previously the generation crashed
earlier with the FillError about 15 items, so the beatability check was never
reached.

### The fix

```python
multiworld.completion_condition[player] = lambda state: state.has(
    "Sky Temple Grounds - Sky Temple Gateway | Victory", player
)
```

---

## Fix 6 — `set_rules`: credits exits connect to wrong region

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
| 1 | `gfmc_compound.py` | Above Ship sub-region unreachable (no inbound exit) | 1 location |
| 2 | `hydrodynamo_station.py` | No trick-free path to Hydrodynamo Shaft | 12+ locations |
| 3 | `dark_forgotten_bridge.py` | No trick-free path to Dark Arena Tunnel after bridge rotation | 2 locations |
| 4 | `judgment_pit.py` | `condition_and` instead of `condition_or` (translator bug) | 2 locations |
| 5 | `logic/__init__.py` | Completion condition checks wrong item name | Game always unbeatable |
| 6 | `logic/__init__.py` | Credits exits self-loop instead of connecting to credits region | Affects disabled/emperor_ing_only modes |
