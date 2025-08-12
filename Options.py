from dataclasses import dataclass

from Options import Choice, DeathLink, OptionList, PerGameCommonOptions, Range, Toggle


class StartLocation(Choice):
    """Choose where you want to start the game."""
    display_name = "Starting Location"
    option_TempleGrounds_LandingSite = 0
    default = 0


class FinalBoss(Choice):
    """Choose which final bosses you fight."""
    display_name = "Final Boss(es)"
    option_all = 0
    option_emperor_ing_only = 1
    option_dark_samus_only = 2
    option_none = 3
    default = 0


class SkyTempleKeyCount(Range):
    """Number of Sky Temple Keys to shuffle. Shuffling 0 artifacts means direct access to Sky Temple."""
    display_name = "Shuffled Sky Temple Key Count"
    range_start = 0
    range_end = 9
    default = 0


class RequireMissileLauncher(Toggle):
    """Do we need Missile Launcher to shoot missiles?"""
    display_name = "Require Missile Launcher"


class RequirePowerBombLauncher(Toggle):
    """Do we need Power Bomb Launcher to lay power bombs?"""
    display_name = "Require Power Bomb Launcher"


class ShuffleScanVisor(Toggle):
    """Do we shuffle Scan Visor?"""
    display_name = "Shuffle Scan Visor"


class ShuffleSpringBall(Choice):
    """Do we shuffle Spring Ball?"""
    display_name = "Shuffle Spring Ball"
    option_disabled = 0
    option_locked_by_bomb = 1
    option_shuffled = 2
    default = 0


class RemoveMissileCoverAtSaveStation(Toggle):
    """Do we remove missile cover at save station?"""
    display_name = "Remove missile cover at save station"


class Tricks(OptionList):
    """Which tricks are enabled?"""
    display_name = "Tricks"
    options = [
        "Sky Temple Grounds - Abandoned Base | Slope Jump to Portal",
        "Sky Temple Grounds - Base Access | DBJ to Top",
        "Sky Temple Grounds - Phazon Grounds | Visorless Invisible Platforms",
        "Sky Temple Grounds - Phazon Pit | BSJ to Phazon Grounds Side",
        "Sky Temple Grounds - Phazon Pit | DBJ to Profane Path Side",
        "Sky Temple Grounds - Plains of Dark Worship | Suitless SA to Item",
        "Sky Temple Grounds - Profane Path | DBJ to Sky Temple Side",
        "Temple Grounds - Communication Area | DBJ from Bottom to Item Ledge",
        "Temple Grounds - Communication Area | Standable Terrain from Bottom to Item Ledge",
        "Temple Grounds - Communication Area | DBJ from Item Ledge to Top",
        "Temple Grounds - Communication Area | NSJ SA from Item Ledge to Top",
        "Temple Grounds - Dynamo Chamber | DBJ over Communication Area Side gate",
        "Temple Grounds - Dynamo Chamber | SJ over Communication Area Side gate",
        "Temple Grounds - Fortress Transport Access | IS to get item",
        "Temple Grounds - GFMC Compound | DBJ to Sacred Bridge Ledge",
        "Temple Grounds - GFMC Compound | DBJ to Windchamber Tunnel Ledge",
        "Temple Grounds - GFMC Compound | Slope Jump to Sacred Bridge Ledge",
        "Temple Grounds - Grand Windchamber | 3BSJ then SA from Windchamber Tunnel Side to Platform",
        "Temple Grounds - Grand Windchamber | SA from Cannon to Platform",
        "Temple Grounds - Hall of Eyes | DBJ to Top",
        "Temple Grounds - Hall of Honored Dead | Instant Morph to Morph Tunnel",
        "Temple Grounds - Hall of Honored Dead | SA into Morph Tunnel",
        "Temple Grounds - Hall of Honored Dead | Spinners with PB",
        "Temple Grounds - Industrial Site | DBJ from Center to Collapsed Tunnel Ledge",
        "Temple Grounds - Industrial Site | Open Gate from Center with Charged Annihilator Beam",
        "Temple Grounds - Industrial Site | Open Gate from Center with Charge Beam",
        "Temple Grounds - Industrial Site | Open Gate from Center with Missiles",
        "Temple Grounds - Hive Chamber A | Out of Bounds",
        "Temple Grounds - Landing Site | Light Beam Block Skip"
        "Temple Grounds - Meeting Grounds | To top with Screw Attack",
        "Temple Grounds - Path of Eyes | BSJ from Center to Waterway",
        "Temple Grounds - Path of Eyes | DBJ to skip SJ",
        "Temple Grounds - Path of Eyes | Light Beam Block Skip at Waterway",
        "Temple Grounds - Sacred Bridge | SJ from Center to Sacred Path Side",
        "Temple Grounds - Sacred Path | DBJ to Great Temple Side",
        "Temple Grounds - Temple Assembly Site | DBJ to Item Ledge",
        "Temple Grounds - Temple Assembly Site | NSJ SA to Item Ledge",
        "Temple Grounds - Temple Assembly Site | Slope Jump to Item Ledge",
        "Temple Grounds - Trooper Security Station | SA to break the gate",

        #Agon Wastes
        "Agon Wastes - Agon Temple | Break Glass to Temple Access with SA",
        "Agon Wastes - Agon Temple | Break Glass to Temple Access with Boost Ball",
        "Agon Wastes - Agon Temple | Slope Jump over Glass to Temple Access",
        "Agon Wastes - Agon Temple | Break Glass to Temple Access with SA on Z-Axis",
        "Agon Wastes - Agon Temple | Break Glass to Controller Access with SA",
        "Agon Wastes - Agon Temple | Break Glass to Controller Access with Boost Ball",
        "Agon Wastes - Agon Temple | Slope Jump over Glass to Controller Access",
        "Agon Wastes - Agon Temple | Break Glass to Controller Access with SA on Z-Axis",
        "Agon Wastes - Agon Temple | Bomb Guardian with Missiles",
        "Agon Wastes - Agon Temple | Bomb Guardian with PBs",
        "Agon Wastes - Agon Temple | Bomb Guardian with Dark Beam",
        "Agon Wastes - Agon Temple | Bomb Guardian with SA",
        "Agon Wastes - Biostorage Station | Jump to Top Level from Crates",
        "Agon Wastes - Biostorage Station | TBJS to Top Level",
        "Agon Wastes - Biostorage Station | SA Recoil up to Top Level",
        "Agon Wastes - Central Station Access | DBJ to Mining Station A Ledge",
        "Agon Wastes - Central Station Access | SA on Z-Axis to Mining Station Ledge",
        "Agon Wastes - Central Station Access | Wall Boost to Mining Station A Ledge",
        "Agon Wastes - Command Center | Scan/Combat Dash over Gap to Security Station B",
        "Agon Wastes - Command Center | NSJ SA over Gap to Security Station B",
        "Agon Wastes - Command Center Access | DBJ from Under Grates to Command Center Access Bottom",
        "Agon Wastes - Command Center Access | Wall Boost from Under Grates to Command Center Access Bottom",
        "Agon Wastes - Command Center Access | Standable from Under Grates to Command Center Bottom",
        "Agon Wastes - Controller Access | Bomb Slot without Bombs",
        "Agon Wastes - Mine Shaft | Wall Boost up to Mine Shaft Top",
        "Agon Wastes - Mining Station A | DBJ to Central Station Access Platform",
        "Agon Wastes - Mining Station A | NSJ SA to Temple Access Ledge",
        "Agon Wastes - Mining Station A | SA Z-Axis to Temple Access Ledge",
        "Agon Wastes - Mining Station A | Combat/Scan Dash to Temple Access Ledge",
        "Agon Wastes - Mining Station A | Extended Dash to Temple Access Ledge",
        "Agon Wastes - Mining Station A | Boost Jump to Temple Access Ledge",
        "Agon Wastes - Mining Station A | 3BSJ to Standable Terrain",
        "Agon Wastes - Mining Station A | DBJ to Scan Post",
        "Agon Wastes - Mining Station A | DBJ to Central Station Access Ledge",
        "Agon Wastes - Mining Station A | Combat/Scan Dash to Central Station Access Ledge",
        "Agon Wastes - Mining Station A | 2BSJ over Gate",
        "Agon Wastes - Mining Station A | SA Bonk over Gate",
        "Agon Wastes - Mining Station B | BSJ up to Portal",
        "Agon Wastes - Mining Station B | SA to Portal",
        "Agon Wastes - Mining Station B | Slope Jump to Portal",
        "Agon Wastes - Mining Station B | Out of Bounds",
        "Agon Wastes - Mining Station B | DBJS to Item before Puzzle",
        "Agon Wastes - Mining Station B | SA Cancel to Item",
        "Agon Wastes - Mining Station B | Slope Jump to Standable Terrain",
        "Agon Wastes - Mining Station B | SBSJ to Item Ledge",
        "Agon Wastes - Mining Station B | TBJ to Standable Terrain from Portal Platform",
        "Agon Wastes - Mining Station B | 2BSJ to Standable Terrain from Portal Platform",
        "Agon Wastes - Mining Station B | SA from Cannon Standable Terrain to Item",
        "Agon Wastes - Mining Station B | Slope Jump to Portal Cover then Combat/Scan Dash to Item",
        "Agon Wastes - Mining Station B | SA from Standable Terrain to Top Bomb Slot",
        "Agon Wastes - Mining Station B | Slope Jump to Top Bomb Slot",
        "Agon Wastes - Mining Station B | Bomb Slots without Bombs",
        "Agon Wastes - Mining Station B | Instant Morph into Bottom Bomb Slot",
        "Agon Wastes - Mining Station B | Wall Boost into Bottom Bomb Slot",
        "Agon Wastes - Portal Terminal | Activate Portal Without Bombs",
        "Agon Wastes - Portal Terminal | Activate Portal Without Bombs NSJ",
        "Agon Wastes - Sandcanyon | Terminal Fall Abuse",
        "Agon Wastes - Sand Processing | DBJ up to Save Station C"
        "Agon Wastes - Sand Processing | NSJ SA Slope Jump to Save Station C",
        "Agon Wastes - Sand Processing | TBSJ up to Save Station C",
        "Agon Wastes - Sand Processing | SA Slope Jump up to Save Station C",
        "Agon Wastes - Sand Processing | 2BSJ up to Morph Tunnel Ledge",
        "Agon Wastes - Sand Processing | SA over to Morph Tunnel Ledge",
        "Agon Wastes - Sand Processing | Wall Boost into Morph Tunnel",
        "Agon Wastes - Sand Processing | SA into Morph Tunnel",
        "Agon Wastes - Sand Processing | Wall Boost into Morph Tunnel",
        "Agon Wastes - Sand Processing | SA into Morph Tunnel",
        "Agon Wastes - Sand Processing | Bomb Slot without Bombs",
        "Agon Wastes - Security Station A | Bomb Slot without Bombs",
        "Agon Wastes - Transit Station | Break Rocks with Boost Ball",
        "Agon Wastes - Transit Station | Out of Bounds",
        "Agon Wastes - Transport Center | Bomb Slot without Bombs",
        "Agon Wastes - Transport Center | Slope Jump SA to Transport to Torvus Bog",
        "Agon Wastes - Transport Center | Halfpipe Standable up to Tranpsort to Torvus Bog",
        "Agon Wastes - Transport Center | Instant Morph to Instant Unmorph Jump to Transport to Torvus Bog",
        "Agon Wastes - Ventilation Area B | Disable Lasers from Out of Bounds",
        "Agon Wastes - Ventilation Area B | Out of Bounds to Save Station C Side",
    ]


@dataclass
class MetroidPrime2Options(PerGameCommonOptions):
    start_location: StartLocation
    final_bosses: FinalBoss
    sky_temple_keys_count: SkyTempleKeyCount
    require_missile_launcher: RequireMissileLauncher
    require_power_bomb_launcher: RequirePowerBombLauncher
    shuffle_scan_visor: ShuffleScanVisor
    shuffle_spring_ball: ShuffleSpringBall
    remove_missile_cover_at_save_station: RemoveMissileCoverAtSaveStation
    tricks: Tricks
    death_link: DeathLink
