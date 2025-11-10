import glob
import importlib
import inspect
import os
import re
from itertools import chain
from pathlib import Path
from types import ModuleType
from typing import Iterable, TypeVar


T = TypeVar('T')


def get_all_classes_from_modules(mods: list[ModuleType], type: T) -> list[T]:
    def get_all_classes_from_module(mod: ModuleType) -> Iterable[T]:
        ret = []
        for name, obj in inspect.getmembers(mod, inspect.isclass):
            if obj.__module__ == mod.__name__:
                ret.append(obj)
        return ret

    return list(chain.from_iterable([
        get_all_classes_from_module(mod)
        for mod in mods
    ]))


def import_all_submodules(mod: ModuleType) -> list[ModuleType]:
    path = Path(os.path.dirname(mod.__file__))
    submodules = glob.glob(str(path) + "/*.py")
    submodules = [os.path.basename(f)[:-3] for f in submodules if
                  os.path.isfile(f) and not os.path.basename(f).startswith('__')]  # exclude __init__.py
    ret = []
    for submodule in submodules:
        ret.append(importlib.import_module(f'.{submodule}', mod.__name__))
    return ret


def condition_or(conditions: list[bool]) -> bool:
    result = False
    for condition in conditions:
        result = result or condition
    return result


def condition_and(conditions: list[bool]) -> bool:
    result = True
    for condition in conditions:
        if not (result and condition):
            return False
    return result


def items_start_id() -> int:
    return 0xDEAFBABE


def locations_start_id() -> int:
    return items_start_id() + 150


def strip_description_from_region_name(region_name: str):
    tmp = region_name.split(" - ")
    if len(tmp) != 2:
        raise Exception(f"Are you stripping description from a region name? (region_name: {region_name})")

    # Strip description if it exists
    part_to_remove = re.findall("\\(([^)]+)\\)", tmp[1])
    if part_to_remove is not None and len(part_to_remove) > 0:
        tmp[1] = tmp[1].replace(f" ({part_to_remove[0]})", "").strip()

    return f"{tmp[0]} - {tmp[1]}"
