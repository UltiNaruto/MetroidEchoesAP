from .temple_grounds.agon_transport_access import *
from .temple_grounds.collapsed_tunnel import *
from .temple_grounds.command_chamber import *
from .temple_grounds.communication_area import *
from .temple_grounds.dynamo_chamber import *
from .temple_grounds.fortress_transport_access import *
from .temple_grounds.gfmc_compound import *
from .temple_grounds.grand_windchamber import *
from .temple_grounds.hall_of_eyes import *
from .temple_grounds.hall_of_honored_dead import *
from .temple_grounds.hive_access_tunnel import *
from .temple_grounds.hive_chamber_a import *
from .temple_grounds.hive_chamber_b import *
from .temple_grounds.hive_chamber_c import *
from .temple_grounds.hive_save_station import *
from .temple_grounds.hive_storage import *
from .temple_grounds.hive_transport_area import *
from .temple_grounds.hive_tunnel import *
from .temple_grounds.industrial_site import *
from .temple_grounds.landing_site import *
from .temple_grounds.meeting_grounds import *
from .temple_grounds.path_of_eyes import *
from .temple_grounds.path_of_honor import *
from .temple_grounds.sacred_bridge import *
from .temple_grounds.sacred_path import *
from .temple_grounds.service_access import *
from .temple_grounds.storage_cavern_a import *
from .temple_grounds.storage_cavern_b import *
from .temple_grounds.temple_assembly_site import *
from .temple_grounds.temple_transport_a import TempleTransportA as TempleGrounds_TempleTransportA
from .temple_grounds.temple_transport_b import TempleTransportB as TempleGrounds_TempleTransportB
from .temple_grounds.temple_transport_c import TempleTransportC as TempleGrounds_TempleTransportC
from .temple_grounds.torvus_transport_access import TorvusTransportAccess as TempleGrounds_TorvusTransportAccess
from .temple_grounds.transport_to_agon_wastes import TransportToAgonWastes as TempleGrounds_TransportToAgonWastes
from .temple_grounds.transport_to_torvus_bog import TransportToTorvusBog as TempleGrounds_TransportToTorvusBog
from .temple_grounds.transport_to_sanctuary_fortress import TransportToSanctuaryFortress as TempleGrounds_TransportToSanctuaryFortress
from .temple_grounds.trooper_security_station import *
from .temple_grounds.windchamber_gateway import *
from .temple_grounds.windchamber_tunnel import *


def temple_grounds_rooms(player: int, multiworld: MultiWorld) -> list[MetroidPrime2Region]:
    region_name = "Temple Grounds"

    return [
        # Temple Grounds - Agon Transport Access
        AgonTransportAccess(region_name, player, multiworld),

        # Temple Grounds - Collapsed Tunnel
        CollapsedTunnel_IndustrialSiteSide(region_name, player, multiworld),
        CollapsedTunnel_TempleAssemblySiteSide(region_name, player, multiworld),

        # Temple Grounds - Command Chamber
        CommandChamber(region_name, player, multiworld),

        # Temple Grounds - Communication Area
        CommunicationArea_Bottom(region_name, player, multiworld),
        CommunicationArea_ItemLedge(region_name, player, multiworld),
        CommunicationArea_Top(region_name, player, multiworld),

        # Temple Grounds - Dynamo Chamber
        DynamoChamber_BetweenItemGates(region_name, player, multiworld),
        DynamoChamber_Center(region_name, player, multiworld),
        DynamoChamber_CommunicationAreaSide(region_name, player, multiworld),
        DynamoChamber_Item(region_name, player, multiworld),
        DynamoChamber_TempleAssemblySiteSide(region_name, player, multiworld),

        # Temple Grounds - Fortress Transport Access
        FortressTransportAccess_Bottom(region_name, player, multiworld),
        FortressTransportAccess_Top(region_name, player, multiworld),

        # Temple Grounds - GFMC Compound
        GFMCCompound_AboveShip(region_name, player, multiworld),
        GFMCCompound_BehindTranslatorGate(region_name, player, multiworld),
        GFMCCompound_Center(region_name, player, multiworld),
        GFMCCompound_Cutscene(region_name, player, multiworld),
        GFMCCompound_SacredBridgeLedge(region_name, player, multiworld),
        GFMCCompound_TrooperSecurityStationSide(region_name, player, multiworld),
        GFMCCompound_WindchamberTunnelLedge(region_name, player, multiworld),

        # Temple Grounds - Grand Windchamber
        GrandWindchamber_Cannon(region_name, player, multiworld),
        GrandWindchamber_Platform(region_name, player, multiworld),
        GrandWindchamber_WindchamberGatewaySide(region_name, player, multiworld),
        GrandWindchamber_WindchamberTunnelSide(region_name, player, multiworld),

        # Temple Grounds - Hall of Eyes
        HallOfEyes_Bottom(region_name, player, multiworld),
        HallOfEyes_Top(region_name, player, multiworld),

        # Temple Grounds - Hall of Honored Dead
        HallOfHonoredDead(region_name, player, multiworld),
        HallOfHonoredDead_PathOfHonorSide(region_name, player, multiworld),

        # Temple Grounds - Hive Access Tunnel
        HiveAccessTunnel_HiveTransportAreaSide(region_name, player, multiworld),
        HiveAccessTunnel_LandingSiteSide(region_name, player, multiworld),

        # Temple Grounds - Hive Chamber A
        HiveChamberA(region_name, player, multiworld),
        HiveChamberA_DarkMissileTrooper(region_name, player, multiworld),

        # Temple Grounds - Hive Chamber B
        HiveChamberB(region_name, player, multiworld),
        HiveChamberB_BehindBombCover(region_name, player, multiworld),

        # Temple Grounds - Hive Chamber C
        HiveChamberC(region_name, player, multiworld),

        # Temple Grounds - Hive Save Station
        HiveSaveStation(region_name, player, multiworld),

        # Temple Grounds - Hive Storage
        HiveStorage(region_name, player, multiworld),

        # Temple Grounds - Hive Transport Area
        HiveTransportArea_BehindTranslatorGate(region_name, player, multiworld),
        HiveTransportArea_Bottom(region_name, player, multiworld),
        HiveTransportArea_Top(region_name, player, multiworld),

        # Temple Grounds - Hive Tunnel
        HiveTunnel(region_name, player, multiworld),

        # Temple Grounds - Industrial Site
        IndustrialSite_BehindTranslatorGate(region_name, player, multiworld),
        IndustrialSite_Center(region_name, player, multiworld),
        IndustrialSite_CollapsedTunnelLedge(region_name, player, multiworld),
        IndustrialSite_FrontOfTranslatorGate(region_name, player, multiworld),
        IndustrialSite_Gate(region_name, player, multiworld),
        IndustrialSite_HiveTransportAreaSide(region_name, player, multiworld),

        # Temple Grounds - Landing Site
        LandingSite_Bottom(region_name, player, multiworld),
        LandingSite_Top(region_name, player, multiworld),

        # Temple Grounds - Meeting Grounds
        MeetingGrounds_Bottom(region_name, player, multiworld),
        MeetingGrounds_GreatTempleSide(region_name, player, multiworld),
        MeetingGrounds_Top(region_name, player, multiworld),

        # Temple Grounds - Path of Eyes
        PathOfEyes_Center(region_name, player, multiworld),
        PathOfEyes_HallOfEyesSide(region_name, player, multiworld),
        PathOfEyes_TorvusTransportAccessSide(region_name, player, multiworld),
        PathOfEyes_TranslatorGate(region_name, player, multiworld),
        PathOfEyes_UTurn(region_name, player, multiworld),
        PathOfEyes_Waterway(region_name, player, multiworld),
        PathOfEyes_WindchamberGatewaySide(region_name, player, multiworld),

        # Temple Grounds - Path of Honor
        PathOfHonor_Bottom(region_name, player, multiworld),
        PathOfHonor_Top(region_name, player, multiworld),

        # Temple Grounds - Sacred Bridge
        SacredBridge_Center(region_name, player, multiworld),
        SacredBridge_GFMCCompoundSide(region_name, player, multiworld),
        SacredBridge_SacredPathSide(region_name, player, multiworld),

        # Temple Grounds - Sacred Path
        SacredPath_GreatTempleSide(region_name, player, multiworld),
        SacredPath_PortalLedge(region_name, player, multiworld),
        SacredPath_SacredBridgeSide(region_name, player, multiworld),

        # Temple Grounds - Service Access
        ServiceAccess_Bottom_MeetingGroundsSide(region_name, player, multiworld),
        ServiceAccess_Bottom_PathOfHonorSide(region_name, player, multiworld),
        ServiceAccess_Bottom_Tunnel(region_name, player, multiworld),
        ServiceAccess_Top_MeetingGroundsSide(region_name, player, multiworld),
        ServiceAccess_Top_PathOfHonorSide(region_name, player, multiworld),

        # Temple Grounds - Storage Cavern A
        StorageCavernA(region_name, player, multiworld),

        # Temple Grounds - Storage Cavern B
        StorageCavernB(region_name, player, multiworld),

        # Temple Grounds - Temple Assembly Site
        TempleAssemblySite_BehindLightBeamBlock(region_name, player, multiworld),
        TempleAssemblySite_BehindTranslatorGate(region_name, player, multiworld),
        TempleAssemblySite_Center(region_name, player, multiworld),
        TempleAssemblySite_CollapsedTunnelSide(region_name, player, multiworld),
        TempleAssemblySite_DynamoChamberLedge(region_name, player, multiworld),
        TempleAssemblySite_ItemLedge(region_name, player, multiworld),
        TempleAssemblySite_StorageCavernBSide(region_name, player, multiworld),

        # Temple Grounds - Temple Transport A
        TempleGrounds_TempleTransportA(region_name, player, multiworld),

        # Temple Grounds - Temple Transport B
        TempleGrounds_TempleTransportB(region_name, player, multiworld),

        # Temple Grounds - Temple Transport C
        TempleGrounds_TempleTransportC(region_name, player, multiworld),

        # Temple Grounds - Torvus Transport Access
        TempleGrounds_TorvusTransportAccess(region_name, player, multiworld),

        # Temple Grounds - Transport to Agon Wastes
        TempleGrounds_TransportToAgonWastes(region_name, player, multiworld),

        # Temple Grounds - Transport to Sanctuary Fortress
        TempleGrounds_TransportToSanctuaryFortress(region_name, player, multiworld),

        # Temple Grounds - Transport to Torvus Bog
        TempleGrounds_TransportToTorvusBog(region_name, player, multiworld),

        # Temple Grounds - Trooper Security Station
        TrooperSecurityStation_CommunicationAreaSide(region_name, player, multiworld),
        TrooperSecurityStation_GFMCCompoundSide(region_name, player, multiworld),

        # Temple Grounds - Windchamber Gateway
        WindchamberGateway_GrandWindchamberSide(region_name, player, multiworld),
        WindchamberGateway_PathOfEyesSide(region_name, player, multiworld),
        WindchamberGateway_Platform(region_name, player, multiworld),

        # Temple Grounds - Windchamber Tunnel
        WindchamberTunnel_GFMCCompoundSide(region_name, player, multiworld),
        WindchamberTunnel_GrandWindchamberSide(region_name, player, multiworld),
    ]