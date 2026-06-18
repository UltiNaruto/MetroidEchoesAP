from BaseClasses import MultiWorld, ItemClassification
from ... import has_trick_enabled, can_lay_bomb
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class CatacombsAccess_CatacombsSide(MetroidPrime2Region):
    name="Catacombs Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs (Keybearer Ledge)",
            door=DoorCover.Dark,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs Access (Hydrodynamo Station Side)",
            rule=lambda state, player: condition_or([
                state.has("Space Jump Boots", player),
                can_lay_bomb(state, player)
            ])
        )
    ]


class CatacombsAccess_HydrodynamoStationSide(MetroidPrime2Region):
    name="Hydrodynamo Station Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Hydrodynamo Station (East Door Ledge)",
            door=DoorCover.Dark,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Torvus Bog - Catacombs Access (Catacombs Side)",
            rule=lambda state, player: True
        )
    ]
