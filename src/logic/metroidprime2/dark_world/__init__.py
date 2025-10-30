from .sky_temple_grounds.accursed_lake import *
from .sky_temple_grounds.abandoned_base import *
from .sky_temple_grounds.base_access import *
from .sky_temple_grounds.defiled_shrine import *
from .sky_temple_grounds.gateway_access import *
from .sky_temple_grounds.ing_windchamber import *
from .sky_temple_grounds.ing_reliquary import *
from .sky_temple_grounds.lake_access import *
from .sky_temple_grounds.phazon_grounds import *
from .sky_temple_grounds.phazon_pit import *
from .sky_temple_grounds.plain_of_dark_worship import *
from .sky_temple_grounds.profane_path import *
from .sky_temple_grounds.reliquary_access import *
from .sky_temple_grounds.reliquary_grounds import *
from .sky_temple_grounds.shrine_access import *
from .sky_temple_grounds.sky_temple_gateway import *
from .sky_temple_grounds.war_ritual_grounds import *


def sky_temple_grounds_rooms(player: int, multiworld: MultiWorld) -> list[MetroidPrime2Region]:
    region_name = "Sky Temple Grounds"

    return [
        # Sky Temple Grounds - Accursed Lake
        AccursedLake(region_name, player, multiworld),
        AccursedLake_IngCache(region_name, player, multiworld),

        # Sky Temple Grounds - Abandoned Base
        AbandonedBase(region_name, player, multiworld),
        AbandonedBase_Platform(region_name, player, multiworld),
        AbandonedBase_Portal(region_name, player, multiworld),

        # Sky Temple Grounds - Base Access
        BaseAccess_Bottom(region_name, player, multiworld),
        BaseAccess_Top(region_name, player, multiworld),

        # Sky Temple Grounds - Defiled Shrine
        DefiledShrine(region_name, player, multiworld),
        DefiledShrine_IngCache(region_name, player, multiworld),
        DefiledShrine_SafeZone(region_name, player, multiworld),

        # Sky Temple Grounds - Gateway Access
        GatewayAccess_SafeZone(region_name, player, multiworld),
        GatewayAccess_ShrineAccessSide(region_name, player, multiworld),
        GatewayAccess_SkyTempleGatewaySide(region_name, player, multiworld),

        # Sky Temple Grounds - Ing Windchamber
        IngWindchamber_East(region_name, player, multiworld),
        IngWindchamber_North(region_name, player, multiworld),
        IngWindchamber_Portal(region_name, player, multiworld),
        IngWindchamber_West(region_name, player, multiworld),

        # Sky Temple Grounds - Ing Reliquary
        IngReliquary(region_name, player, multiworld),
        IngReliquary_IngCache(region_name, player, multiworld),

        # Sky Temple Grounds - Lake Access
        LakeAccess(region_name, player, multiworld),

        # Sky Temple Grounds - Phazon Grounds
        PhazonGrounds(region_name, player, multiworld),
        PhazonGrounds_Item(region_name, player, multiworld),

        # Sky Temple Grounds - Phazon Pit
        PhazonPit_PhazonGroundsSide(region_name, player, multiworld),
        PhazonPit_ProfanePathSide(region_name, player, multiworld),

        # Sky Temple Grounds - Plain of Dark Worship
        PlainOfDarkWorship(region_name, player, multiworld),
        PlainOfDarkWorship_Item(region_name, player, multiworld),

        # Sky Temple Grounds - Profane Path
        ProfanePath_Item(region_name, player, multiworld),
        ProfanePath_PhazonPitSide(region_name, player, multiworld),
        ProfanePath_PortalLedge(region_name, player, multiworld),
        ProfanePath_SkyTempleSide(region_name, player, multiworld),

        # Sky Temple Grounds - Reliquary Access
        ReliquaryAccess_PhazonGroundsSide(region_name, player, multiworld),
        ReliquaryAccess_ReliquaryGroundsSide(region_name, player, multiworld),

        # Sky Temple Grounds - Reliquary Grounds
        ReliquaryGrounds_Bottom(region_name, player, multiworld),
        ReliquaryGrounds_Top(region_name, player, multiworld),

        # Sky Temple Grounds - Shrine Access
        ShrineAccess_SafeZone(region_name, player, multiworld),
        ShrineAccess_WarRitualGroundsSide(region_name, player, multiworld),

        # Sky Temple Grounds - Sky Temple Gateway
        SkyTempleGateway(region_name, player, multiworld),
        SkyTempleGateway_Credits(region_name, player, multiworld),
        SkyTempleGateway_DarkSamusFight(region_name, player, multiworld),
        SkyTempleGateway_GatewayAccessSide(region_name, player, multiworld),

        # Sky Temple Grounds - War Ritual Grounds
        WarRitualGrounds_BaseAccessSide(region_name, player, multiworld),
        WarRitualGrounds_Item(region_name, player, multiworld),
        WarRitualGrounds_SafeZone(region_name, player, multiworld),
        WarRitualGrounds_ShrineAccessSide(region_name, player, multiworld),
    ]