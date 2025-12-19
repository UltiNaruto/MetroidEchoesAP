from BaseClasses import ItemClassification, MultiWorld

from ... import can_activate_light_beam_block, can_lay_bomb, has_trick_enabled
from ..... import MetroidPrime2Item
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class PathOfEyes_Center(MetroidPrime2Region):
    name = "Path of Eyes"
    desc = "Center"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Path of Eyes (U Turn)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has("Temple Grounds - Path of Eyes | Light Beam Block 2 Opened", player),
                condition_or([
                    state.has("Space Jump Boots", player),
                    condition_and([
                        has_trick_enabled(state, player, "Temple Grounds - Path of Eyes | DBJ to skip SJ"),
                        can_lay_bomb(state, player),
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Path of Eyes (Waterway)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                condition_and([
                    has_trick_enabled(state, player, "Temple Grounds - Path of Eyes | BSJ from Center to Waterway"),
                    can_lay_bomb(state, player),
                    state.has("Space Jump Boots", player),
                ]),
                condition_and([
                    state.has("Temple Grounds - Path of Eyes | Light Beam Block 2 Opened", player),
                    condition_or([
                        state.has("Space Jump Boots", player),
                        condition_and([
                            has_trick_enabled(state, player, "Temple Grounds - Path of Eyes | DBJ to skip SJ"),
                            can_lay_bomb(state, player),
                        ]),
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Path of Eyes (Windchamber Gateway Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Temple Grounds - Path of Eyes | Light Beam Block To Windchamber Gateway Opened", player),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Light Beam Block 2",
            locked_item=MetroidPrime2Item(
                name="Temple Grounds - Path of Eyes | Light Beam Block 2 Opened",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: can_activate_light_beam_block(state, player),
        )
        self.add_location(
            name="Light Beam Block To Windchamber Gateway",
            locked_item=MetroidPrime2Item(
                name="Temple Grounds - Path of Eyes | Light Beam Block To Windchamber Gateway Opened",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: can_activate_light_beam_block(state, player),
        )


class PathOfEyes_HallOfEyesSide(MetroidPrime2Region):
    name = "Path of Eyes"
    desc = "Hall of Eyes Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Hall of Eyes (Top)",
            door=DoorCover.SuperMissile,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Path of Eyes (U Turn)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has("Temple Grounds - Path of Eyes | Light Beam Block 1 Opened", player),
                condition_or([
                    state.has("Space Jump Boots", player),
                    condition_and([
                        has_trick_enabled(state, player, "Temple Grounds - Path of Eyes | DBJ to skip SJ"),
                        can_lay_bomb(state, player),
                    ]),
                ]),
            ])
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Path of Eyes (Translator Gate)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                state.has_all({
                    "Temple Grounds - Path of Eyes | Light Beam Block Shortcut Opened",
                    "Morph Ball",
                }, player),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Light Beam Block 1",
            locked_item=MetroidPrime2Item(
                name="Temple Grounds - Path of Eyes | Light Beam Block 1 Opened",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: can_activate_light_beam_block(state, player),
        )


class PathOfEyes_TorvusTransportAccessSide(MetroidPrime2Region):
    name = "Path of Eyes"
    desc = "Torvus Transport Access Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Path of Eyes (Translator Gate)",
            door=DoorCover.AmberTranslator,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Torvus Transport Access",
            door=DoorCover.Any,
            rule=lambda state, player: True,
        ),
    ]


class PathOfEyes_TranslatorGate(MetroidPrime2Region):
    name = "Path of Eyes"
    desc = "Translator Gate"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Path of Eyes (Waterway)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Path of Eyes (Hall of Eyes Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has_all({
                "Temple Grounds - Path of Eyes | Light Beam Block Shortcut Opened",
                "Morph Ball",
            }, player),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Path of Eyes (Torvus Transport Access Side)",
            door=DoorCover.AmberTranslator,
            rule=lambda state, player: True,
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Light Beam Block Shortcut",
            locked_item=MetroidPrime2Item(
                name="Temple Grounds - Path of Eyes | Light Beam Block Shortcut Opened",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: can_activate_light_beam_block(state, player),
        )


class PathOfEyes_UTurn(MetroidPrime2Region):
    name = "Path of Eyes"
    desc = "U Turn"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Path of Eyes (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                condition_and([
                    has_trick_enabled(state, player, "Temple Grounds - Path of Eyes | DBJ to skip SJ"),
                    can_lay_bomb(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Path of Eyes (Hall of Eyes Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                state.has("Temple Grounds - Path of Eyes | Light Beam Block 1 Opened", player),
                condition_or([
                    state.has("Space Jump Boots", player),
                    condition_and([
                        has_trick_enabled(state, player, "Temple Grounds - Path of Eyes | DBJ to skip SJ"),
                        can_lay_bomb(state, player),
                    ]),
                ]),
            ]),
        ),
    ]


class PathOfEyes_Waterway(MetroidPrime2Region):
    name = "Path of Eyes"
    desc = "Waterway"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Path of Eyes (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: True,
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Path of Eyes (Translator Gate)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                state.has("Space Jump Boots", player),
                condition_or([
                    state.has("Temple Grounds - Path of Eyes | Light Beam Block 3 Opened", player),
                    has_trick_enabled(state, player, "Temple Grounds - Path of Eyes | Light Beam Block Skip at Waterway"),
                ]),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Light Beam Block 3",
            locked_item=MetroidPrime2Item(
                name="Temple Grounds - Path of Eyes | Light Beam Block 3 Opened",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: can_activate_light_beam_block(state, player),
        )


class PathOfEyes_WindchamberGatewaySide(MetroidPrime2Region):
    name = "Path of Eyes"
    desc = "Windchamber Gateway Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Temple Grounds - Path of Eyes (Center)",
            door=DoorCover.Opened,
            rule=lambda state, player: state.has("Temple Grounds - Path of Eyes | Light Beam Block To Windchamber Gateway Opened", player),
        ),
        MetroidPrime2Exit(
            destination="Temple Grounds - Windchamber Gateway (Path of Eyes Side)",
            door=DoorCover.SuperMissile,
            rule=lambda state, player: True,
        ),
    ]
