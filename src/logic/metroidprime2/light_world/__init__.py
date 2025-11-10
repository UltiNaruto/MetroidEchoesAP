from BaseClasses import MultiWorld

from ....Regions import MetroidPrime2Region
from ....Utils import get_all_classes_from_modules, import_all_submodules


def temple_grounds_rooms(player: int, multiworld: MultiWorld) -> list[MetroidPrime2Region]:
    region_name = "Temple Grounds"

    from . import temple_grounds
    rooms = get_all_classes_from_modules(import_all_submodules(temple_grounds), MetroidPrime2Region)

    return [
        room(region_name, player, multiworld)
        for room in rooms
    ]