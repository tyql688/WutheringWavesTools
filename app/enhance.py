import json

from .RESOURCE_PATH import *

special_character = {
    "1604": "漂泊者·湮灭·女",
    "1605": "漂泊者·湮灭·男",
    "1502": "漂泊者·衍射·女",
    "1501": "漂泊者·衍射·男",
}


def enhance():
    with open(RAW_CHARACTER_PATH, 'r', encoding='utf-8') as f:
        all_character = json.load(f)
    with open(RAW_WEAPON_PATH, 'r', encoding='utf-8') as f:
        all_weapon = json.load(f)
    with open(RAW_ECHO_PATH, 'r', encoding='utf-8') as f:
        all_echo = json.load(f)
    _all = {**all_character, **all_weapon, **all_echo}

    result = {_id: detail['zh-Hans'] for _id, detail in _all.items()}
    result.update(special_character)

    with open(ID_NAME_PATH, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    result = {v: k for k, v in result.items()}
    with open(NAME_ID_PATH, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
