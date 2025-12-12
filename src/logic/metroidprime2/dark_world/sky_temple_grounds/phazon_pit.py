from ... import can_lay_bomb, can_use_screw_attack, has_dark_suit, has_light_suit, has_trick_enabled
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class PhazonPit_PhazonGroundsSide(MetroidPrime2Region):
    name = "Phazon Pit"
    desc = "Phazon Grounds Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Phazon Grounds",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Phazon Pit (Sacred Path Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
                # required to cross the gap
                condition_or([
                    state.has_any({
                        "Grapple Beam",
                        "Space Jump Boots"
                    }, player),
                    condition_and([
                        has_trick_enabled(state, player, "Sky Temple Grounds - Phazon Pit | DBJ to Profane Path Side"),
                        can_lay_bomb(state, player),
                    ]),
                ]),
            ]),
        ),
    ]


class PhazonPit_ProfanePathSide(MetroidPrime2Region):
    name = "Phazon Pit"
    desc = "Profane Path Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Phazon Pit (Phazon Grounds Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    state.count("Energy Tank", player) >= 3,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
                # required to cross the gap
                condition_or([
                    condition_and([
                        # consider an additional etank when doing this trick
                        state.count("Energy Tank", player) >= 4,
                        has_trick_enabled(state, player, "Sky Temple Grounds - Phazon Pit | BSJ to Phazon Grounds Side"),
                        state.has("Space Jump Boots", player),
                        can_lay_bomb(state, player),
                    ]),
                    state.has("Grapple Beam", player),
                    can_use_screw_attack(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Sky Temple Grounds - Profane Path (Phazon Pit Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]
