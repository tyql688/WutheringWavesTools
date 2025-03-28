import json

from .RESOURCE_PATH import *
from .char_model import CharModel
from .material_model import MaterialItem
from .utils import lower_first_letter
from .weapon_model import WeaponModel

special_character = {
    "1604": "漂泊者·湮灭·女",
    "1605": "漂泊者·湮灭·男",
    "1502": "漂泊者·衍射·女",
    "1501": "漂泊者·衍射·男",
}

special_character2 = {
    "1604": "漂泊者·湮灭",
    "1605": "漂泊者·湮灭",
    "1502": "漂泊者·衍射",
    "1501": "漂泊者·衍射",
}


def enhance():
    with open(RAW_CHARACTER_PATH, 'r', encoding='utf-8') as f:
        all_character = json.load(f)
    with open(RAW_WEAPON_PATH, 'r', encoding='utf-8') as f:
        all_weapon = json.load(f)
    with open(RAW_ECHO_PATH, 'r', encoding='utf-8') as f:
        all_echo = json.load(f)
    with open(RAW_ITEM_PATH, 'r', encoding='utf-8') as f:
        all_item = json.load(f)
        all_item = {k: v for k, v in all_item.items() if v['tag'][0] in MATERIAL_TAG}
    _all = {**all_character, **all_weapon, **all_echo}

    result = {_id: detail['zh-Hans'] for _id, detail in _all.items()}
    result.update({k: v['name'] for k, v in all_item.items()})
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

    _weapon = {_id: detail['zh-Hans'] for _id, detail in all_weapon.items() if detail['rank'] >= 4}
    with open(WEAPON_ALIAS_PATH, 'r', encoding='utf-8') as f:
        old_weapon = json.load(f)
        for i in _weapon.values():
            if '投影' in i:
                continue
            if i not in old_weapon:
                old_weapon[i] = [i]

    with open(WEAPON_ALIAS_PATH, 'w', encoding='utf-8') as f:
        json.dump(old_weapon, f, ensure_ascii=False, indent=2)


def enhance_role_skill():
    from . import api
    with open(RAW_CHARACTER_PATH, 'r', encoding='utf-8') as f:
        all_character = json.load(f)
    api.download_skill_pic(all_character)


def enhance_role_chain():
    from . import api
    with open(RAW_CHARACTER_PATH, 'r', encoding='utf-8') as f:
        all_character = json.load(f)
    api.download_chain_pic(all_character)


def enhance_weapon():
    with open(RAW_WEAPON_PATH, 'r', encoding='utf-8') as f:
        all_weapon = json.load(f)

    weapon_map = {}
    for weapon_id in all_weapon.keys():
        with open(f"{RAW_RESOURCE_PATH}/{weapon_id}.json", 'r', encoding='utf-8') as f:
            weapon_detail = json.load(f)
        if weapon_detail.get('Skin'):
            continue
        weapon_model = WeaponModel.parse_obj(weapon_detail)
        weapon_map[weapon_id] = lower_first_letter(weapon_model.dict(exclude_none=True))
        print(weapon_map[weapon_id])

    for weapon_id in weapon_map.keys():
        with open(WEAPON_PATH / f'{weapon_id}.json', 'w', encoding='utf-8') as f:
            json.dump(weapon_map[weapon_id], f, ensure_ascii=False, indent=2)


def enhance_char():
    with open(RAW_CHARACTER_PATH, 'r', encoding='utf-8') as f:
        all_char = json.load(f)

    char_map = {}
    for char_id in all_char.keys():
        with open(f"{RAW_RESOURCE_PATH}/{char_id}.json", 'r', encoding='utf-8') as f:
            char_detail = json.load(f)

        if char_id in ["1501", "1502"]:
            continue

        char_model = CharModel.parse_obj(char_detail)
        char_map[char_id] = lower_first_letter(char_model.dict(exclude_none=True))
        print(char_map[char_id])

    for char_id in char_map.keys():
        with open(CHAR_PATH / f'{char_id}.json', 'w', encoding='utf-8') as f:
            json.dump(char_map[char_id], f, ensure_ascii=False, indent=2)


def enhance_material():
    with open(RAW_ITEM_PATH, 'r', encoding='utf-8') as f:
        all_items = json.load(f)

    _map = {}
    for _id in all_items.keys():
        with open(f"{RAW_RESOURCE_PATH}/{_id}.json", 'r', encoding='utf-8') as f:
            _detail = json.load(f)
        if _detail['Tag'][0] not in MATERIAL_TAG:
            continue
        _model = MaterialItem.parse_obj(_detail)
        _map[_id] = lower_first_letter(_model.dict(exclude_none=True))
        print(_map[_id])

    for _id in _map.keys():
        with open(MATERIAL_PATH / f'{_id}.json', 'w', encoding='utf-8') as f:
            json.dump(_map[_id], f, ensure_ascii=False, indent=2)
