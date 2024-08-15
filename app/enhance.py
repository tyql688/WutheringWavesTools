import json

from .RESOURCE_PATH import *

special_character = {
    "1604": "漂泊者·湮灭·女",
    "1605": "漂泊者·湮灭·男",
    "1502": "漂泊者·衍射·女",
    "1501": "漂泊者·衍射·男",
}

special_character2 = {
    "1604": "漂泊者·湮灭",
    "1605": "漂泊者·湮灭",
    "1502": "漂泊者",
    "1501": "漂泊者",
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
    result.update(special_character2)

    with open(ID_NAME_PATH, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    char = {_id: detail['zh-Hans'] for _id, detail in all_character.items()}
    char.update(special_character2)
    with open(CHAR_ID_PATH, 'w', encoding='utf-8') as f:
        char_data = {}
        for i, v in char.items():
            char_data[i] = {
                "name": v
            }
        json.dump(char_data, f, ensure_ascii=False, indent=2)

    with open(CHAR_ALIAS_PATH, 'r', encoding='utf-8') as f:
        old = json.load(f)
        for i in char.values():
            if i not in old:
                old[i] = [i]

    with open(CHAR_ALIAS_PATH, 'w', encoding='utf-8') as f:
        json.dump(old, f, ensure_ascii=False, indent=2)


def enhance_role_detail():
    from . import api
    with open(RAW_CHARACTER_PATH, 'r', encoding='utf-8') as f:
        all_character = json.load(f)
    api.download_skill_pic(all_character)
