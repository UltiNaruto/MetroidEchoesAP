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
        "Great Temple - Temple Sanctuary | Defeat Alpha Splinter with Bombs",
        "Great Temple - Temple Sanctuary | Defeat Alpha Splinter with Boost Ball",
        "Great Temple - Temple Sanctuary | Defeat Alpha Splinter with Power Bomb",
        "Great Temple - Temple Sanctuary | Defeat Alpha Splinter with Screw Attack and SJ",
        "Great Temple - Transport A Access | Break Block with Boost Ball",
        "Great Temple - Transport A Access | Break Block with Screw Attack",
        "Great Temple - Transport A Access | Break Block with Super Missile",
        "Great Temple - Transport B Access | Item with Slope Jump and SJ",
        "Great Temple - Transport B Access | Item with Wall Boost",
        "Sky Temple - Sanctum Access | Z-Axis SA to Top",
        "Sky Temple - Sanctum | Emperor Ing 3 with SA",
        "Sky Temple - Sanctum | Escape with Z-Axis SA",
        "Sky Temple Grounds - Abandoned Base | Slope Jump to Portal",
        "Sky Temple Grounds - Base Access | DBJ to Top",
        "Sky Temple Grounds - Defiled Shrine | DBJ to Top",
        "Sky Temple Grounds - Phazon Grounds | Visorless Invisible Platforms",
        "Sky Temple Grounds - Phazon Pit | BSJ to Phazon Grounds Side",
        "Sky Temple Grounds - Phazon Pit | DBJ to Profane Path Side",
        "Sky Temple Grounds - Plains of Dark Worship | Suitless SA to Item",
        "Sky Temple Grounds - Profane Path | DBJ to Sky Temple Side",
        "Sky Temple Grounds - Shrine Access | Wall Boost",
        "Sky Temple Grounds - Sky Temple Gateway | Dark Samus Fight without Echo Visor",
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
