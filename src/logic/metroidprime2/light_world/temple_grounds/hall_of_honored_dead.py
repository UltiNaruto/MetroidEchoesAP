from BaseClasses import MultiWorld

from ... import (
    can_lay_bomb,
    can_lay_pb,
    can_use_boost_ball,
    can_use_screw_attack,
    has_trick_enabled,
)
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class HallOfHonoredDead(MetroidPrime2Region):
    name = "Hall of Honored Dead"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Hall of Honored Dead (Path of Honor Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    has_trick_enabled(state, player, "Temple Grounds - Hall of Honored Dead | Instant Morph to Morph Tunnel"),
                    state.has_all({
                        "Space Jump Boots",
                        "Morph Ball",
                    }, player),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Temple Grounds - Hall of Honored Dead | SA into Morph Tunnel"),
                    can_use_screw_attack(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Path of Honor (Bottom)",
            door=DoorCover.Seeker,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Seeker Launcher)",
            can_access=lambda state, player: condition_and([
                condition_or([
                    condition_and([
                        has_trick_enabled(state, player, "Temple Grounds - Hall of Honored Dead | Spinners with PB"),
                        can_lay_pb(state, player, 3),
                    ]),
                    can_lay_bomb(state, player),
                ]),
                can_use_boost_ball(state, player),
            ]),
        )


class HallOfHonoredDead_PathOfHonorSide(MetroidPrime2Region):
    name = "Hall of Honored Dead"
    desc = "Path of Honor Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Hall of Honored Dead",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Path of Honor (Top)",
            door=DoorCover.MorphBallTunnel,
            rule=lambda state, player: True,
        ),
    ]
