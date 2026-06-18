from ... import has_missile_count, has_trick_enabled, can_use_seeker_launcher, can_use_screw_attack
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_or, condition_and


class TransportToAgonWastes(MetroidPrime2Region):
    name="Transport to Agon Wastes"
    exits_ = [
        MetroidPrime2Exit(
            destination="Torvus Bog - Torvus Temple (Underground)",
            door=DoorCover.Seeker,
            rule=lambda state, player: condition_or([
                can_use_seeker_launcher(state, player),
                condition_and([
                    has_missile_count(state, player, 5),
                    can_use_screw_attack(state, player),
                    has_trick_enabled(state, player, "Torvus Bog - Torvus Temple | Seeker Skip")
                ])
            ])
        ),
        MetroidPrime2Exit(
            destination="E|Agon Wastes - Transport to Torvus Bog",
            rule=lambda state, player: state.has("Scan Visor", player)
        )
    ]
