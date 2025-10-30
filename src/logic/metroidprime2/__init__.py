from typing import cast

from BaseClasses import CollectionState
from ...Enums import DoorCover
from ...Options import MetroidPrime2Options, FinalBoss
from ...Utils import condition_and, condition_or


def has_dark_ammo(state: CollectionState, player: int) -> bool:
    return state.has_any({
        "Dark Beam",
        "Dark Ammo Expansion",
        "Beam Ammo Expansion",
    }, player)


def has_light_ammo(state: CollectionState, player: int) -> bool:
    return state.has_any({
        "Light Beam",
        "Light Ammo Expansion",
        "Beam Ammo Expansion",
    }, player)


def can_use_grapple_beam(state: CollectionState, player: int) -> bool:
    return state.has("Grapple Beam", player)


def can_use_power_beam(state: CollectionState, player: int) -> bool:
    return condition_or([
        state.has("Power Beam", player),
        state.count("Progressive Power Beam", player) >= 1,
    ])


def can_use_dark_beam(state: CollectionState, player: int) -> bool:
    return condition_or([
        state.has("Dark Beam", player),
        state.count("Progressive Dark Beam", player) >= 1,
    ])


def can_use_light_beam(state: CollectionState, player: int) -> bool:
    return condition_or([
        state.has("Light Beam", player),
        state.count("Progressive Light Beam", player) >= 1,
    ])


def can_use_annihilator_beam(state: CollectionState, player: int) -> bool:
    return condition_and([
        condition_or([
            state.has("Annihilator Beam", player),
            state.count("Progressive Annihilator Beam", player) >= 1,
        ]),
        condition_or([
            # check if we have both dark and light ammo
            condition_and([
                has_dark_ammo(state, player),
                has_light_ammo(state, player),
            ]),
            # in case we need to activate a portal without ammo
            # or if we need to open an annihilator door
            condition_and([
                condition_or([
                    not has_dark_ammo(state, player),
                    not has_light_ammo(state, player),
                ]),
                condition_or([
                    state.has("Charge Beam", player),
                    state.count("Progressive Annihilator Beam", player) >= 2,
                ]),
            ]),
        ]),
    ])


def can_use_charged_power_beam(state: CollectionState, player: int) -> bool:
    return condition_or([
        condition_and([
            state.has("Power Beam", player),
            state.has("Charge Beam", player),
        ]),
        state.count("Progressive Power Beam", player) >= 2,
    ])


def can_use_charged_dark_beam(state: CollectionState, player: int) -> bool:
    return condition_or([
        condition_and([
            state.has("Dark Beam", player),
            state.has("Charge Beam", player),
        ]),
        state.count("Progressive Dark Beam", player) >= 2,
    ])


def can_use_charged_light_beam(state: CollectionState, player: int) -> bool:
    return condition_or([
        condition_and([
            state.has("Light Beam", player),
            state.has("Charge Beam", player),
        ]),
        state.count("Progressive Light Beam", player) >= 2,
    ])


def can_use_charged_annihilator_beam(state: CollectionState, player: int, requires_ammo: bool=False) -> bool:
    return condition_and([
        condition_or([
            condition_and([
                state.has("Annihilator Beam", player),
                state.has("Charge Beam", player),
            ]),
            state.count("Progressive Annihilator Beam", player) >= 2,
        ]),
        # check if we need dark and light ammo
        # if not in fight then no
        condition_or([
            not requires_ammo,
            condition_and([
                requires_ammo,
                has_dark_ammo(state, player),
                has_light_ammo(state, player),
            ]),
        ])
    ])


def can_use_super_missile(state: CollectionState, player: int) -> bool:
    return condition_and([
        condition_or([
            state.has_all({
                "Power Beam",
                "Charge Beam",
                "Super Missile",
            }, player),
            state.count("Progressive Power Beam", player) >= 3,
        ]),
        has_missile_count(state, player, 5),
    ])


def can_use_darkburst(state: CollectionState, player: int) -> bool:
    return condition_and([
        condition_or([
            state.has_all({
                "Dark Beam",
                "Charge Beam",
                "Darkburst",
            }, player),
            state.count("Progressive Dark Beam", player) >= 3,
        ]),
        has_missile_count(state, player, 5),
    ])


def can_use_sunburst(state: CollectionState, player: int) -> bool:
    return condition_and([
        condition_or([
            state.has_all({
                "Light Beam",
                "Charge Beam",
                "Sunburst",
            }, player),
            state.count("Progressive Light Beam", player) >= 3,
        ]),
        has_missile_count(state, player, 5),
    ])


def can_use_sonic_boom(state: CollectionState, player: int) -> bool:
    return condition_and([
        condition_or([
            state.has_all({
                "Annihilator Beam",
                "Charge Beam",
                "Sonic Boom",
            }, player),
            state.count("Progressive Annihilator Beam", player) >= 3,
        ]),
        has_dark_ammo(state, player),
        has_light_ammo(state, player),
        has_missile_count(state, player, 5),
    ])


def can_use_seeker_launcher(state: CollectionState, player: int) -> bool:
    return condition_and([
        state.has("Seeker Launcher", player),
        # consider more missile to start the charging process of Seeker Launcher
        has_missile_count(state, player, 6),
    ])


def can_use_boost_ball(state: CollectionState, player: int) -> bool:
    return state.has_all({
        "Morph Ball",
        "Boost Ball",
    }, player)


def can_use_spider_ball(state: CollectionState, player: int) -> bool:
    return state.has_all({
        "Morph Ball",
        "Spider Ball",
    }, player)


def can_lay_bomb(state: CollectionState, player: int) -> bool:
    return state.has_all({
        "Morph Ball",
        "Morph Ball Bombs",
    }, player)


def can_lay_pb(state: CollectionState, player: int, count: int=1) -> bool:
    return condition_and([
        state.has("Morph Ball", player),
        has_pb_count(state, player, count),
    ])


def can_lay_bomb_or_pb(state: CollectionState, player: int, count: int=1) -> bool:
    return condition_or([
        can_lay_bomb(state, player),
        can_lay_pb(state, player, count),
    ])


def can_use_screw_attack(state: CollectionState, player: int, z_axis: bool=False, is_nsj=False) -> bool:
    return condition_and([
        condition_or([
            is_nsj,
            condition_and([
                z_axis,
                not state.has("Space Jump Boots", player),
            ]),
            state.has("Space Jump Boots", player),
        ]),
        state.has_all({
            "Morph Ball",
            "Screw Attack",
        }, player),
    ])


def get_missile_count(state: CollectionState, player: int) -> int:
    options = cast(MetroidPrime2Options, state.multiworld.worlds[player].options)
    if options.require_missile_launcher.current_option_name == "Yes" and not state.has("Missile Launcher", player):
        return 0
    return state.count("Missile Expansion", player) * 5 + 5 if state.has("Missile Launcher", player) else 0


def has_missile_count(state: CollectionState, player: int, count: int) -> bool:
    return get_missile_count(state, player) >= count


def get_pb_count(state: CollectionState, player: int) -> int:
    options = cast(MetroidPrime2Options, state.multiworld.worlds[player].options)
    if options.require_power_bomb_launcher.current_option_name == "Yes" and not state.has("Power Bomb Launcher", player):
        return 0
    return state.count("Power Bomb Expansion", player) + 4 if state.has("Power Bomb Launcher", player) else 0


def has_pb_count(state: CollectionState, player: int, count: int) -> bool:
    return get_pb_count(state, player) >= count


def has_dark_suit(state: CollectionState, player: int) -> bool:
    return condition_or([
        state.has("Dark Suit", player),
        state.count("Progressive Suit", player) >= 1,
    ])


def has_light_suit(state: CollectionState, player: int) -> bool:
    return condition_or([
        state.has("Light Suit", player),
        state.count("Progressive Suit", player) >= 2,
    ])


def can_destroy_cover(state: CollectionState, player: int, cover: DoorCover) -> bool:
    # noinspection PyUnreachableCode
    match cover:
        case DoorCover.Opened:
            return True
        case DoorCover.Any:
            return condition_or([
                can_use_power_beam(state, player),
                can_use_dark_beam(state, player),
                can_use_light_beam(state, player),
                can_use_annihilator_beam(state, player),
                has_missile_count(state, player, 1),
                can_lay_bomb(state, player),
            ])
        case DoorCover.Missile:
            return has_missile_count(state, player, 1)
        case DoorCover.Seeker:
            return can_use_seeker_launcher(state, player)
        case DoorCover.Power:
            return can_use_power_beam(state, player)
        case DoorCover.Dark:
            return can_use_dark_beam(state, player)
        case DoorCover.Light:
            return can_use_light_beam(state, player)
        case DoorCover.Annihilator:
            return can_use_annihilator_beam(state, player)
        case DoorCover.ChargeBeam_Any:
            return condition_or([
                can_use_charged_power_beam(state, player),
                can_use_charged_dark_beam(state, player),
                can_use_charged_light_beam(state, player),
                can_use_charged_annihilator_beam(state, player),
            ])
        case DoorCover.ChargeBeam_Power:
            return can_use_charged_power_beam(state, player)
        case DoorCover.ChargeBeam_Dark:
            return can_use_charged_dark_beam(state, player)
        case DoorCover.ChargeBeam_Light:
            return can_use_charged_light_beam(state, player)
        case DoorCover.ChargeBeam_Annihilator:
            return can_use_charged_annihilator_beam(state, player)
        case DoorCover.SuperMissile:
            return can_use_super_missile(state, player)
        case DoorCover.Darkburst:
            return can_use_darkburst(state, player)
        case DoorCover.Sunburst:
            return can_use_sunburst(state, player)
        case DoorCover.SonicBoom:
            return can_use_sonic_boom(state, player)
        case DoorCover.MorphBallTunnel:
            return state.has("Morph Ball", player)
        case DoorCover.Bomb:
            return can_lay_bomb(state, player)
        case DoorCover.PowerBomb:
            return can_lay_pb(state, player)
        case DoorCover.ScrewAttack:
            return can_use_screw_attack(state, player)
        case DoorCover.ScanVisor:
            return state.has("Scan Visor", player)
        case DoorCover.DarkVisor:
            return state.has("Dark Visor", player)
        case DoorCover.EchoVisor:
            return state.has("Echo Visor", player)
        case DoorCover.GrappleBeam:
            return state.has("Grapple Beam", player)
        case DoorCover.DoubleDamage:
            return state.has("Double Damage", player)
        case DoorCover.VioletTranslator:
            return state.has("Violet Translator", player)
        case DoorCover.AmberTranslator:
            return state.has("Amber Translator", player)
        case DoorCover.EmeraldTranslator:
            return state.has("Emerald Translator", player)
        case DoorCover.CobaltTranslator:
            return state.has("Cobalt Translator", player)
        case DoorCover.RubyTranslator:
            return state.has("Ruby Translator", player)
        case DoorCover.ObsidianTranslator:
            return state.has("Obsidian Translator", player)
        case other:
            raise Exception(f"Unknown door cover {other}!")


def can_activate_dark_portal(state: CollectionState, player: int) -> bool:
    return condition_or([
        can_use_charged_dark_beam(state, player),
        can_use_charged_annihilator_beam(state, player),
    ])


def can_activate_light_portal(state: CollectionState, player: int) -> bool:
    # Always check if player has Charge Beam in case the player runs out of ammo
    return condition_or([
        can_use_charged_light_beam(state, player),
        can_use_charged_annihilator_beam(state, player),
    ])


def can_activate_light_beam_block(state: CollectionState, player: int) -> bool:
    return can_use_light_beam(state, player)


def can_activate_safe_zone(state: CollectionState, player: int) -> bool:
    return condition_or([
        can_use_charged_annihilator_beam(state, player),
        can_use_charged_light_beam(state, player),
        can_use_power_beam(state, player),
    ])


def has_enough_sky_temple_keys(state: CollectionState, player: int) -> bool:
    options = cast(MetroidPrime2Options, state.multiworld.worlds[player].options)
    needed_sky_temple_keys_count: int = options.sky_temple_keys_count.value
    sky_temple_keys_count: int = sum([1 for i in range(9) if state.has(f'Sky Temple Key {i}', player)])

    return sky_temple_keys_count >= needed_sky_temple_keys_count


def must_fight_emperor_ing(state: CollectionState, player: int) -> bool:
    options = cast(MetroidPrime2Options, state.multiworld.worlds[player].options)

    return options.final_bosses.value in [FinalBoss.option_emperor_ing_only, FinalBoss.option_all]


def must_fight_dark_samus_3_4(state: CollectionState, player: int) -> bool:
    options = cast(MetroidPrime2Options, state.multiworld.worlds[player].options)

    return options.final_bosses.value in [FinalBoss.option_dark_samus_only, FinalBoss.option_all]


def has_trick_enabled(state: CollectionState, player: int, trick_name: str) -> bool:
    options = cast(MetroidPrime2Options, state.multiworld.worlds[player].options)

    return trick_name in options.tricks.value


def has_oob_kit(state: CollectionState, player: int) -> bool:
    return condition_and([
        can_lay_bomb(state, player),
        state.has("Space Jump Boots", player),
    ])
