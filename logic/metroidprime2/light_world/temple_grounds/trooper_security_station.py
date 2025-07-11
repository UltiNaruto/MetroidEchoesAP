from ... import can_lay_bomb_or_pb, can_lay_pb, can_use_boost_ball, can_use_screw_attack, has_trick_enabled
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class TrooperSecurityStation_CommunicationAreaSide(MetroidPrime2Region):
    name = "Trooper Security Station"
    desc = "Communication Area Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Communication Area (Bottom)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - GFMC Compound (Cutscene)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                has_trick_enabled(state, player, "Temple Grounds - Trooper Security Station | IS into GFMC Compound"),
                # expects that the player never touched the cutscene trigger before
                not state.has("Temple Grounds - GFMC Compound | Cutscene Watched", player),
                # expects the player to be able to get Infinite Speed at Temple Grounds - Storage Cavern A
                state.can_reach(spot="Temple Grounds - Storage Cavern A", player=player),
                # needed for Infinite Speed to activate it
                can_use_boost_ball(state, player),
                # expect the player to be able to open the doors in between Storage Cavern A and GFMC Compound
                can_lay_bomb_or_pb(state, player, 1),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Trooper Security Station (GFMC Compound Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                can_lay_pb(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Temple Grounds - Trooper Security Station | SA to break the gate"),
                    can_use_screw_attack(state, player),
                ]),
            ]),
        ),
    ]


class TrooperSecurityStation_GFMCCompoundSide(MetroidPrime2Region):
    name = "Trooper Security Station"
    desc = "GFMC Compound Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - GFMC Compound (Trooper Security Station Side)",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Trooper Security Station (Communication Area Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                can_lay_pb(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Temple Grounds - Trooper Security Station | SA to break the gate"),
                    can_use_screw_attack(state, player),
                ]),
            ]),
        ),
    ]
