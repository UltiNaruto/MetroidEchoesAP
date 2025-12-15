import glob
import importlib
import inspect
import os
import re
import zipfile
from itertools import chain
from pathlib import Path
from types import ModuleType
from typing import Iterable, Optional, TypeVar, Union


T = TypeVar('T')


def _extract_paths_from(path: str) -> tuple[str, Optional[str]]:
    if '.apworld' in path:
        tmp_index = path.find(f'.apworld/')
        if tmp_index == -1:
            tmp_index = path.find(f'.apworld\\')
        if tmp_index == -1:
            raise RuntimeError("Shouldn't happen! Couldn't get apworld separator index for apworld path and inner path!")
        tmp_index += len('.apworld/')
        apworld_path = path[:tmp_index-1]
        return f'{path[tmp_index:].replace("\\", "/")}', apworld_path
    else:
        return path, None


def _import_all_submodules(mod: Union[str, ModuleType], parent_submodule="") -> list[ModuleType]:
    # Shouldn't happen but keep it for safety
    if parent_submodule.endswith('.'):
        return []

    if type(mod) is str:
        if Path(mod).suffix != '':
            mod = os.path.dirname(mod)
        path, apworld_path = _extract_paths_from(mod)
        if parent_submodule == "":
            parent_submodule = f"{__package__}.{os.path.basename(path)}"
    elif type(mod) is ModuleType:
        path, apworld_path = _extract_paths_from(os.path.dirname(mod.__file__))
        if parent_submodule == "":
            parent_submodule = f"{__package__}.{os.path.basename(path)}"
    else:
        raise RuntimeError("Shouldn't happen, but import_all_submodules first argument is not str or ModuleType!")

    # we want either folders or python modules
    if apworld_path is None:
        submodules = glob.glob(f"{path}/*")
        submodules = [
            *[os.path.basename(f) for f in submodules if # exclude __init__.py
             (os.path.isfile(f) and not os.path.basename(f).startswith('__') and Path(f).suffix == ".py")],
            *[os.path.basename(f) for f in submodules
              if os.path.isdir(f)],
        ]
    else:
        submodules = []
        with zipfile.ZipFile(apworld_path) as apworld:
            for f in apworld.namelist():
                # add files if they are in the current directory
                # else only add directory of current directory for recursivity
                if f.startswith(path):
                    rel_path = f.replace(f'{path}\\'.replace('\\', '/'), '')
                    # no need to parse an empty rel_path
                    if rel_path == '':
                        continue
                    # for folders zipfile keeps a separator at the end so remove it
                    if rel_path.endswith('/'):
                        rel_path = rel_path[:-1]
                    if not '/' in rel_path and not Path(f).name.startswith('__') and Path(f).suffix in ['.py', '']:
                        submodules.append(rel_path)

    ret = []
    for submodule in submodules:
        if not submodule.endswith(".py"):
            submodule_path = str(Path(path).joinpath(submodule))
            if apworld_path is not None:
                submodule_path = str(Path(apworld_path).joinpath(submodule_path))
            ret.extend(_import_all_submodules(submodule_path, f'{parent_submodule}.{os.path.basename(submodule)}'))
        else:
            ret.append(importlib.import_module(f".{submodule[:-3]}", parent_submodule))
    return ret


def get_all_classes_from_parent_module(mod: ModuleType, _type: T) -> list[T]:
    def get_all_classes_from_module(m: ModuleType) -> Iterable[T]:
        ret = []
        for name, obj in inspect.getmembers(m, inspect.isclass):
            if obj.__module__ == m.__name__:
                ret.append(obj)
        return ret

    mods = _import_all_submodules(mod)
    return sorted(list(chain.from_iterable([
        get_all_classes_from_module(mod)
        for mod in mods
    ])), key=lambda x: x.__name__)


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
    tmp = region_name.split(" - ", 1)
    if len(tmp) != 2:
        raise Exception(f"Are you stripping description from a region name? (region_name: {region_name})")

    # Strip description if it exists
    part_to_remove = re.findall("\\(([^)]+)\\)", tmp[1])
    if part_to_remove is not None and len(part_to_remove) > 0:
        tmp[1] = tmp[1].replace(f" ({part_to_remove[0]})", "").strip()

    return f"{tmp[0]} - {tmp[1]}"

def snake_case_to_title_case(s: str) -> str:
    tmp = [f'{_[0].upper()}{_[1:]}' for _ in s.split("_")]
    return " ".join(tmp)