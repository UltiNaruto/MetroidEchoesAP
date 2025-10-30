import json
import logging
import os
import pkgutil

from pathlib import Path

from BaseClasses import Entrance, Item, ItemClassification, Location, MultiWorld, Region, Tutorial
from .Items import MetroidPrime2Item, SKY_TEMPLE_KEYS
from .Locations import MetroidPrime2Location
from .Options import MetroidPrime2Options
from .Regions import MetroidPrime2Region
from .Utils import items_start_id, locations_start_id
from .logic import regions_, set_rules, locations
from ..AutoWorld import World, WebWorld


logger = logging.getLogger("Metroid Prime 2 Echoes")


def assert_apworld_properly_installed() -> None:
    path = Path(__file__).parent.resolve()
    parent_path = path.parent.parent.as_posix()
    lib_worlds_path = parent_path.replace("custom_worlds", f"lib/worlds/{os.path.basename(path.as_posix())}.apworld")
    if parent_path.endswith("lib/worlds"):
        raise RuntimeError("This apworld isn't allowed to be placed in lib/worlds."
                           "Please install this apworld through the launcher or place it in custom_worlds.")
    if parent_path.endswith("custom_worlds") and os.path.exists(lib_worlds_path):
        os.remove(lib_worlds_path)


class MetroidPrime2Web(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Metroid Prime Client on your computer. This guide covers single-player, multiworld, and related software.",
        "English",
        "setup_en.md",
        "setup/en",
        ["UltiNaruto"]
    )]


class MetroidPrime2World(World):
    game = "Metroid Prime 2 Echoes"
    topology_present = False
    data_version = 1
    options_dataclass = MetroidPrime2Options
    options: MetroidPrime2Options
    items: dict[str, dict[str, str | int | bool | list[int]]] = json.loads(
        str(pkgutil.get_data(__name__, "data/items/metroidprime2.json"), 'utf-8')
    )
    item_name_to_id = {key: items_start_id() + value["index"] for key, value in items.items()}
    location_name_to_id = {loc_name: locations_start_id() + idx for idx, loc_name in enumerate(locations())}
    web = MetroidPrime2Web()
    required_client_version = (0, 6, 1)

    apworld_version = (0, 1, 0)
    start_location = "Temple Grounds - Landing Site"
    seed: int
    elevators: list[Entrance]
    portals: list[Entrance]

    def __init__(self, multiworld: "MultiWorld", player: int):
        assert_apworld_properly_installed()

        super().__init__(multiworld, player)
        self.elevators = []
        self.portals = []

    def generate_early(self) -> None:
        self.seed = self.random.randrange(99999999)

        # Those aren't shuffled (except scan visor which can be shuffled)
        self.multiworld.push_precollected(self.create_item("Power Suit"))
        self.multiworld.push_precollected(self.create_item("Power Beam"))
        self.multiworld.push_precollected(self.create_item("Combat Visor"))
        if self.options.shuffle_scan_visor.current_option_name == "No":
            self.multiworld.push_precollected(self.create_item("Scan Visor"))

        # Starting area
        match self.options.start_location.current_option_name.lower():
            case "templegrounds landingsite":
                self.start_location = "Temple Grounds - Landing Site (Bottom)"

    def create_items(self) -> None:
        # Initializing item pool as vanilla
        itempool = []
        for item_name, item in self.items.items():
            for _ in range(item["default_shuffled_count"]):
                itempool.append(item_name)

        # Remove extra sky temple keys to free up some space
        # for fillers in item pool
        for i in range(9 - self.options.sky_temple_keys_count.value):
            itempool.remove(SKY_TEMPLE_KEYS[self.sky_temple_keys_count + i])
            itempool.append("Missile Expansion")

        if self.options.shuffle_scan_visor.current_option_name == "Yes":
            itempool.remove("Missile Expansion")
            itempool.append("Scan Visor")

        if self.options.shuffle_spring_ball.current_option_name.lower() == "shuffled":
            itempool.remove("Missile Expansion")
            itempool.append("Spring Ball")

        # remove starting items from item pool
        items_to_exclude = [excluded_items.name
                            for excluded_items in self.multiworld.precollected_items[self.player]]

        for item in items_to_exclude:
            if item in itempool:
                itempool.remove(item)

        itempool = list(map(lambda name: self.create_item(name), itempool))

        # Mark 5 missile expansions as progression
        missile_expansions = [idx for idx, val in enumerate(itempool) if val.name == "Missile Expansion"]
        for idx in range(max(5, len(missile_expansions))):
            itempool[missile_expansions[idx]].classification = ItemClassification.progression

        self.multiworld.itempool += itempool

    def create_item(self, name: str, location: Location | None = None) -> Item:
        try:
            i = self.items[name]
        except KeyError:
            classification = ItemClassification.progression
            if name == "Nothing":
                classification = ItemClassification.filler

            # this is an event item
            item = Item(name, classification, None, self.player)
            if location is not None:
                item.location = location
            return item

        classification = ItemClassification.filler
        if i["progression"] == "progression":
            classification = ItemClassification.progression
        elif i["progression"] == "useful":
            classification = ItemClassification.useful

        return MetroidPrime2Item(name, classification, self.item_name_to_id[name], self.player)

    def set_rules(self) -> None:
        set_rules(self.multiworld, self.player)

    def get_filler_item_name(self) -> str:
        return "Nothing"

    def create_regions(self):
        regions = regions_(self.player, self.multiworld)

        menu = Region("Menu", self.player, self.multiworld)
        credits_outro = Region("Credits - Outro", self.player, self.multiworld)

        # Create all regions
        self.multiworld.regions.append(menu)
        self.multiworld.regions.append(credits_outro)
        for _, region in regions.items():
            for _, room in region.items():
                self.multiworld.regions += [room]
                for loc in room.locations:
                    loc.show_in_spoiler = loc.address is not None

        # Connect starting area
        menu.connect(self.multiworld.get_region(self.start_location, self.player), None, lambda state: True)

        # Connect all the remaining regions
        for region_name, region in regions.items():
            for room_name, room in region.items():
                for exit_ in room.exits_:
                    # Remove the exit if destination is None
                    if exit_.destination is not None:
                        is_elevator = exit_.destination.startswith('E|')
                        is_portal = exit_.destination.startswith('P|')

                        destination = exit_.destination
                        if is_elevator or is_portal:
                            destination = destination[2:]

                        new_exit = room.create_exit(f"{room.name} -> {destination}")
                        new_exit.connect(self.multiworld.get_region(destination, self.player))
                        if is_elevator:
                            self.elevators.append(new_exit)
                        if is_portal:
                            self.portals.append(new_exit)

    def fill_slot_data(self):
        options_dict = self.options.as_dict(
            "start_location",
            "final_bosses",
            "sky_temple_keys_count",
            "require_missile_launcher",
            "require_power_bomb_launcher",
            "shuffle_scan_visor",
            "shuffle_spring_ball",
            "remove_missile_cover_at_save_station",
            "death_link",
        )
        options_dict.update({
            "seed": self.seed,
        })
        return options_dict
