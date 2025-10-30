import re


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
