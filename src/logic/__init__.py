from typing import cast

from BaseClasses import CollectionState, Entrance, MultiWorld
from .metroidprime2 import can_destroy_cover
from ..Enums import DoorCover
from ..Options import MetroidPrime2Options
from ..Regions import MetroidPrime2Exit, MetroidPrime2Region
from ..Utils import condition_and
from ...generic.Rules import set_rule


def regions_(player: int, multiworld: MultiWorld) -> dict[str, dict[str, MetroidPrime2Region]]:
    from .metroidprime2.dark_world import sky_temple_grounds_rooms
    from .metroidprime2.light_world import temple_grounds_rooms

    return {
        'Temple Grounds': {room.name: room for room in temple_grounds_rooms(player, multiworld)},
        'Sky Temple Grounds': {room.name: room for room in sky_temple_grounds_rooms(player, multiworld)},
        #'Great Temple': {room.name: room for room in great_temple_rooms(player, multiworld)},
        #'Sky Temple': {room.name: room for room in sky_temple_rooms(player, multiworld)},
        #'Agon Wastes': {room.name: room for room in agon_wastes_rooms(player, multiworld)},
        #'Dark Agon Wastes': {room.name: room for room in dark_agon_wastes_rooms(player, multiworld)},
        #'Torvus Bog': {room.name: room for room in torvus_bog_rooms(player, multiworld)},
        #'Dark Torvus Bog': {room.name: room for room in dark_torvus_bog_rooms(player, multiworld)},
        #'Sanctuary Fortress': {room.name: room for room in sanctuary_fortress_rooms(player, multiworld)},
        #'Ing Hive': {room.name: room for room in ing_hive_rooms(player, multiworld)},
    }

def locations() -> list[str]:
    return [
        "Temple Grounds - Hive Chamber A - Pickup (Missile Expansion)",
        "Temple Grounds - Hall of Honored Dead - Pickup (Seeker Launcher)",
        "Temple Grounds - Hive Chamber B - Pickup (Missile Expansion)",
        "Sky Temple Grounds - War Ritual Grounds - Pickup (Missile Expansion)",
        "Temple Grounds - Windchamber Gateway - Pickup (Energy Tank)",
        "Temple Grounds - Transport to Agon Wastes - Pickup (Missile Expansion)",
        "Temple Grounds - Temple Assembly Site - Pickup (Missile Expansion)",
        "Temple Grounds - Grand Windchamber - Pickup (Sunburst)",
        "Temple Grounds - Dynamo Chamber - Pickup (Power Bomb Expansion)",
        "Temple Grounds - Storage Cavern B - Pickup (Energy Tank)",
        "Sky Temple Grounds - Plain of Dark Worship - Pickup (Missile Expansion)",
        "Sky Temple Grounds - Defiled Shrine - Pickup (Sky Temple Key 8)",
        "Temple Grounds - Communication Area - Pickup (Missile Expansion)",
        "Temple Grounds - GFMC Compound - Pickup (Missile Launcher)",
        "Temple Grounds - GFMC Compound - Pickup (Missile Expansion)",
        "Sky Temple Grounds - Accursed Lake - Pickup (Sky Temple Key 9)",
        "Temple Grounds - Fortress Transport Access - Pickup (Energy Tank)",
        "Sky Temple Grounds - Profane Path - Pickup (Beam Ammo Expansion)",
        "Sky Temple Grounds - Phazon Grounds - Pickup (Missile Expansion)",
        "Sky Temple Grounds - Ing Reliquary - Pickup (Sky Temple Key 7)",
        "Great Temple - Transport A Access - Pickup (Missile Expansion)",
        "Great Temple - Temple Sanctuary - Pickup (Energy Transfer Module)",
        "Great Temple - Transport B Access - Pickup (Missile Expansion)",
        "Great Temple - Main Energy Controller - Pickup (Light Suit)",
        "Great Temple - Main Energy Controller - Pickup (Violet Translator)",
        "Agon Wastes - Mining Plaza - Pickup (Energy Tank)",
        "Agon Wastes - Mining Station Access - Pickup (Energy Tank)",
        "Agon Wastes - Mining Station B - Pickup (Darkburst)",
        "Agon Wastes - Transport Center - Pickup (Missile Expansion)",
        "Agon Wastes - Mining Station A - Pickup (Missile Expansion)",
        "Dark Agon Wastes - Ing Cache 4 - Pickup (Missile Expansion)",
        "Dark Agon Wastes - Junction Site - Pickup (Missile Expansion)",
        "Agon Wastes - Storage A - Pickup (Missile Expansion)",
        "Agon Wastes - Mine Shaft - Pickup (Energy Tank)",
        "Dark Agon Wastes - Crossroads - Pickup (Missile Expansion)",
        "Agon Wastes - Sand Cache - Pickup (Missile Expansion)",
        "Agon Wastes - Portal Access A - Pickup (Missile Expansion)",
        "Dark Agon Wastes - Judgment Pit - Pickup (Space Jump Boots)",
        "Agon Wastes - Agon Temple - Pickup (Morph Ball Bomb)",
        "Dark Agon Wastes - Trial Tunnel - Pickup (Dark Agon Key 1)",
        "Agon Wastes - Central Mining Station - Pickup (Beam Ammo Expansion)",
        "Dark Agon Wastes - Warrior's Walk - Pickup (Missile Expansion)",
        "Agon Wastes - Sandcanyon - Pickup (Power Bomb Expansion)",
        "Dark Agon Wastes - Dark Agon Temple - Pickup (Dark Suit)",
        "Dark Agon Wastes - Battleground - Pickup (Dark Agon Key 3)",
        "Dark Agon Wastes - Battleground - Pickup (Sky Temple Key 1)",
        "Agon Wastes - Agon Energy Controller - Pickup (Amber Translator)",
        "Agon Wastes - Ventilation Area A - Pickup (Missile Expansion)",
        "Agon Wastes - Command Center - Pickup (Missile Expansion)",
        "Agon Wastes - Main Reactor - Pickup (Missile Expansion)",
        "Dark Agon Wastes - Doomed Entry - Pickup (Dark Agon Key 2)",
        "Agon Wastes - Sand Processing - Pickup (Missile Expansion)",
        "Agon Wastes - Storage D - Pickup (Dark Beam)",
        "Dark Agon Wastes - Dark Oasis - Pickup (Sky Temple Key 2)",
        "Agon Wastes - Storage B - Pickup (Missile Expansion)",
        "Dark Agon Wastes - Feeding Pit - Pickup (Power Bomb Expansion)",
        "Agon Wastes - Bioenergy Production - Pickup (Energy Tank)",
        "Dark Agon Wastes - Ing Cache 1 - Pickup (Light Beam)",
        "Agon Wastes - Storage C - Pickup (Missile Expansion)",
        "Dark Agon Wastes - Ing Cache 2 - Pickup (Sonic Boom)",
        "Torvus Bog - Torvus Lagoon - Pickup (Missile Expansion)",
        "Torvus Bog - Portal Chamber - Pickup (Missile Expansion)",
        "Torvus Bog - Path of Roots - Pickup (Missile Expansion)",
        "Torvus Bog - Forgotten Bridge - Pickup (Missile Expansion)",
        "Torvus Bog - Great Bridge - Pickup (Power Bomb Expansion)",
        "Dark Torvus Bog - Cache A - Pickup (Beam Ammo Expansion)",
        "Torvus Bog - Plaza Access - Pickup (Missile Expansion)",
        "Torvus Bog - Abandoned Worksite - Pickup (Missile Expansion)",
        "Dark Torvus Bog - Poisoned Bog - Pickup (Sky Temple Key 3)",
        "Dark Torvus Bog - Venomous Pond - Pickup (Dark Temple Key 3)",
        "Torvus Bog - Temple Access - Pickup (Energy Tank)",
        "Torvus Bog - Torvus Plaza - Pickup (Energy Tank)",
        "Dark Torvus Bog - Putrid Alcove - Pickup (Power Bomb Expansion)",
        "Torvus Bog - Torvus Grove - Pickup (Missile Expansion)",
        "Torvus Bog - Torvus Temple - Pickup (Super Missile)",
        "Dark Torvus Bog - Dark Torvus Arena - Pickup (Boost Ball)",
        "Dark Torvus Bog - Dark Torvus Arena - Pickup (Dark Torvus Key 1)",
        "Torvus Bog - Underground Tunnel - Pickup (Missile Expansion)",
        "Torvus Bog - Meditation Vista - Pickup (Energy Tank)",
        "Dark Torvus Bog - Dark Torvus Temple - Pickup (Dark Visor)",
        "Dark Torvus Bog - Cache B - Pickup (Energy Tank)",
        "Torvus Bog - Hydrodynamo Station - Pickup (Missile Expansion)",
        "Torvus Bog - Torvus Energy Controller - Pickup (Emerald Translator)",
        "Dark Torvus Bog - Undertemple Access - Pickup (Dark Torvus Key 1)",
        "Torvus Bog - Gathering Hall - Pickup (Missile Expansion)",
        "Torvus Bog - Training Chamber - Pickup (Missile Expansion)",
        "Dark Torvus Bog - Sacrificial Chamber - Pickup (Grapple Beam)",
        "Dark Torvus Bog - Undertemple - Pickup (Missile Expansion)",
        "Dark Torvus Bog - Undertemple - Pickup (Power Bomb)",
        "Torvus Bog - Transit Tunnel South - Pickup (Missile Expansion)",
        "Torvus Bog - Transit Tunnel East - Pickup (Energy Tank)",
        "Dark Torvus Bog - Dungeon - Pickup (Sky Temple Key 4)",
        "Torvus Bog - Hydrochamber Storage - Pickup (Gravity Boost)",
        "Dark Torvus Bog - Undertransit One - Pickup (Missile Expansion)",
        "Sanctuary Fortress - Sanctuary Entrance - Pickup (Power Bomb Expansion)",
        "Sanctuary Fortress - Reactor Core - Pickup (Energy Tank)",
        "Sanctuary Fortress - Transit Station - Pickup (Power Bomb Expansion)",
        "Sanctuary Fortress - Sanctuary Map Station - Pickup (Missile Expansion)",
        "Sanctuary Fortress - Hall of Combat Mastery - Pickup (Missile Expansion)",
        "Sanctuary Fortress - Main Research - Pickup (Missile Expansion)",
        "Ing Hive - Culling Chamber - Pickup (Ing Hive Key 1)",
        "Sanctuary Fortress - Central Area Transport West - Pickup (Missile Expansion)",
        "Sanctuary Fortress - Dynamo Works - Pickup (Spider Ball)",
        "Sanctuary Fortress - Dynamo Works - Pickup (Missile Expansion)",
        "Ing Hive - Hazing Cliff - Pickup (Missile Expansion)",
        "Sanctuary Fortress - Watch Station - Pickup (Beam Ammo Expansion)",
        "Ing Hive - Hive Dynamo Works - Pickup (Sky Temple Key 6)",
        "Sanctuary Fortress - Sentinel's Path - Pickup (Missile Expansion)",
        "Sanctuary Fortress - Watch Station Access - Pickup (Energy Tank)",
        "Ing Hive - Aerial Training Site - Pickup (Ing Hive Key 3)",
        "Ing Hive - Aerial Training Site - Pickup (Missile Expansion)",
        "Sanctuary Fortress - Main Gyro Chamber - Pickup (Power Bomb Expansion)",
        "Sanctuary Fortress - Vault - Pickup (Screw Attack)",
        "Sanctuary Fortress - Temple Access - Pickup (Missile Expansion)",
        "Ing Hive - Hive Gyro Chamber - Pickup (Ing Hive Key 2)",
        "Ing Hive - Hive Temple - Pickup (Annihilator Beam)",
        "Sanctuary Fortress - Sanctuary Energy Controller - Pickup (Cobalt Translator)",
        "Ing Hive - Hive Entrance - Pickup (Sky Temple Key 5)",
        "Sanctuary Fortress - Aerie - Pickup (Echo Visor)",
    ]


def _set_rule(entrance: Entrance, exit_: MetroidPrime2Exit, player: int):
    def exit_rule(state: CollectionState) -> bool:
        condition = exit_.rule(state, player),

        # add a door condition if it's not a sub region transition
        if exit_.door != DoorCover.Opened:
            condition = condition_and([
                can_destroy_cover(state, player, exit_.door),
                exit_.rule(state, player),
            ])

        return condition

    set_rule(entrance, lambda state: exit_rule(state))


def set_rules(multiworld: MultiWorld, player: int):
    options = cast(MetroidPrime2Options, multiworld.worlds[player].options)
    regions = [region for region in multiworld.get_regions() if region.player == player and region.__class__.__base__ is MetroidPrime2Region]
    credits_outro = multiworld.get_region("Credits - Outro", player)

    region: MetroidPrime2Region
    for region in regions:
        for exit_ in region.exits_:
            if exit_.destination is not None:
                is_elevator = exit_.destination.startswith('E|')
                is_portal = exit_.destination.startswith('P|')

                destination = exit_.destination
                if is_elevator or is_portal:
                    destination = destination[2:]

                _set_rule(multiworld.get_entrance(f"{region.name} -> {destination}", player), exit_, player)

    # Switch Sky Temple Gateway destination to Credits if final bosses are off
    if options.final_bosses.current_option_name.lower() == "disabled":
        sky_temple_gateway = multiworld.get_region("Sky Temple Grounds - Sky Temple Gateway", player)
        exit_to_credits = sky_temple_gateway.create_exit(f"{sky_temple_gateway.name} -> {credits_outro.name}")
        exit_to_credits.connect(sky_temple_gateway)
    elif options.final_bosses.current_option_name.lower() == "emperor ing only":
        sky_temple_energy_controller = multiworld.get_region("Sky Temple - Sky Temple Energy Controller", player)
        exit_to_credits = sky_temple_energy_controller.create_exit(f"{sky_temple_energy_controller.name} -> {credits_outro.name}")
        exit_to_credits.connect(sky_temple_energy_controller)

    multiworld.completion_condition[player] = lambda state: state.has("Victory", player)
