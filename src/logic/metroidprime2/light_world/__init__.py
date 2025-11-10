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

def great_temple_rooms(player: int, multiworld: MultiWorld) -> list[MetroidPrime2Region]:
    region_name = "Great Temple"

    from . import great_temple
    rooms = get_all_classes_from_modules(import_all_submodules(great_temple), MetroidPrime2Region)

    return [
        room(region_name, player, multiworld)
        for room in rooms
    ]

def agon_wastes_rooms(player: int, multiworld: MultiWorld) -> list[MetroidPrime2Region]:
    region_name = "Agon Wastes"

    from . import agon_wastes
    rooms = get_all_classes_from_modules(import_all_submodules(agon_wastes), MetroidPrime2Region)

    return [
        room(region_name, player, multiworld)
        for room in rooms
    ]

def torvus_bog_rooms(player: int, multiworld: MultiWorld) -> list[MetroidPrime2Region]:
    region_name = "Torvus Bog"

    from . import torvus_bog
    rooms = get_all_classes_from_modules(import_all_submodules(torvus_bog), MetroidPrime2Region)

    return [
        room(region_name, player, multiworld)
        for room in rooms
    ]

def sanctuary_fortress_rooms(player: int, multiworld: MultiWorld) -> list[MetroidPrime2Region]:
    region_name = "Sanctuary Fortress"

    from . import sanctuary_fortress
    rooms = get_all_classes_from_modules(import_all_submodules(sanctuary_fortress), MetroidPrime2Region)

    return [
        room(region_name, player, multiworld)
        for room in rooms
    ]