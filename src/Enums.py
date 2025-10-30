from enum import IntEnum


class DoorCover(IntEnum):
    Opened = -1
    """Used for transitioning between sub regions"""
    Any = 0
    """Blue door, vulnerable to anything"""
    Missile = 1
    Seeker = 2
    Power = 3
    Dark = 4
    Light = 5
    Annihilator = 6
    ChargeBeam_Any = 7
    ChargeBeam_Power = 8
    ChargeBeam_Dark = 9
    ChargeBeam_Light = 10
    ChargeBeam_Annihilator = 11
    SuperMissile = 12
    Darkburst = 13
    Sunburst = 14
    SonicBoom = 15
    MorphBallTunnel = 16
    Bomb = 17
    PowerBomb = 18
    ScrewAttack = 19
    ScanVisor = 20
    DarkVisor = 21
    EchoVisor = 22
    GrappleBeam = 23
    DoubleDamage = 24
    # used for translator gates
    VioletTranslator = 25
    AmberTranslator = 26
    EmeraldTranslator = 27
    CobaltTranslator = 28
    RubyTranslator = 29
    ObsidianTranslator = 30