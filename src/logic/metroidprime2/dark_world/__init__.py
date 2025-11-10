from BaseClasses import MultiWorld

from ....Regions import MetroidPrime2Region
from ....Utils import get_all_classes_from_modules, import_all_submodules


def dark_agon_wastes_rooms(player: int, multiworld: MultiWorld) -> list[MetroidPrime2Region]:
    region_name = "Dark Agon Wastes"

    from . import dark_agon_wastes
    rooms = get_all_classes_from_modules(import_all_submodules(dark_agon_wastes), MetroidPrime2Region)

    return [
        room(region_name, player, multiworld)
        for room in rooms
    ]


def dark_torvus_bog_rooms(player: int, multiworld: MultiWorld) -> list[MetroidPrime2Region]:
    region_name = "Dark Torvus Bog"

    from . import dark_torvus_bog
    rooms = get_all_classes_from_modules(import_all_submodules(dark_torvus_bog), MetroidPrime2Region)

    return [
        room(region_name, player, multiworld)
        for room in rooms
    ]


def ing_hive_rooms(player: int, multiworld: MultiWorld) -> list[MetroidPrime2Region]:
    region_name = "Ing Hive"

    from . import ing_hive
    rooms = get_all_classes_from_modules(import_all_submodules(ing_hive), MetroidPrime2Region)

    return [
        room(region_name, player, multiworld)
        for room in rooms
    ]


def sky_temple_rooms(player: int, multiworld: MultiWorld) -> list[MetroidPrime2Region]:
    region_name = "Sky Temple"

    from . import sky_temple
    rooms = get_all_classes_from_modules(import_all_submodules(sky_temple), MetroidPrime2Region)

    return [
        room(region_name, player, multiworld)
        for room in rooms
    ]


def sky_temple_grounds_rooms(player: int, multiworld: MultiWorld) -> list[MetroidPrime2Region]:
    region_name = "Sky Temple Grounds"

    from . import sky_temple_grounds
    rooms = get_all_classes_from_modules(import_all_submodules(sky_temple_grounds), MetroidPrime2Region)

    return [
        room(region_name, player, multiworld)
        for room in rooms
    ]