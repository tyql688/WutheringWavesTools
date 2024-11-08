import json

from .RESOURCE_PATH import *
from .char_model import CharModel

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

    _weapon = {_id: detail['zh-Hans'] for _id, detail in all_weapon.items() if detail['rank'] >= 4}
    with open(WEAPON_ALIAS_PATH, 'r', encoding='utf-8') as f:
        old_weapon = json.load(f)
        for i in _weapon.values():
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


class WeaponData:
    def __int__(self):
        self.name = None
        self.starLevel = None
        self.type = None
        self.stats = None
        self.effect = None
        self.effectName = None
        self.param = None

    def toDict(self):
        return {
            "name": self.name,
            "starLevel": self.starLevel,
            "type": self.type,
            "stats": self.stats,
            "effect": self.effect,
            "effectName": self.effectName,
            "param": self.param,
        }


def enhance_weapon():
    def lower_first_letter(data):
        if isinstance(data, dict):
            new_dict = {}
            for key, value in data.items():
                new_key = key[0].lower() + key[1:]
                new_dict[new_key] = lower_first_letter(value)
            return new_dict
        elif isinstance(data, list):
            return [lower_first_letter(item) for item in data]
        else:
            return data

    with open(RAW_WEAPON_PATH, 'r', encoding='utf-8') as f:
        all_weapon = json.load(f)

    weapon_map = {}
    for weapon_id in all_weapon.keys():
        with open(f"{RAW_RESOURCE_PATH}/{weapon_id}.json", 'r', encoding='utf-8') as f:
            weapon_detail = json.load(f)

        weapon = WeaponData()
        weapon.name = weapon_detail['Name']
        weapon.starLevel = weapon_detail['Rarity']
        weapon.type = weapon_detail['Type']
        # weapon.stats = weapon_detail['Stats']
        weapon.stats = lower_first_letter(weapon_detail['Stats'])
        weapon.effect = weapon_detail['Effect']
        weapon.effectName = weapon_detail['EffectName']
        weapon.param = weapon_detail['Param']
        weapon_map[weapon_id] = weapon.toDict()

    # with open(WEAPON_PATH, 'w', encoding='utf-8') as f:
    #     json.dump(weapon_map, f, ensure_ascii=False)

    for weapon_id in weapon_map.keys():
        with open(WEAPON_PATH / f'{weapon_id}.json', 'w', encoding='utf-8') as f:
            json.dump(weapon_map[weapon_id], f, ensure_ascii=False)


def enhance_char():
    def lower_first_letter(data):
        if isinstance(data, dict):
            new_dict = {}
            for key, value in data.items():
                new_key = key[0].lower() + key[1:]
                new_dict[new_key] = lower_first_letter(value)
            return new_dict
        elif isinstance(data, list):
            return [lower_first_letter(item) for item in data]
        else:
            return data

    with open(RAW_CHARACTER_PATH, 'r', encoding='utf-8') as f:
        all_char = json.load(f)

    char_map = {}
    for char_id in all_char.keys():
        with open(f"{RAW_RESOURCE_PATH}/{char_id}.json", 'r', encoding='utf-8') as f:
            char_detail = json.load(f)

        char_model = CharModel.parse_obj(char_detail)
        char_map[char_id] = lower_first_letter(char_model.dict(exclude_none=True))
        print(char_map[char_id])

    for char_id in char_map.keys():
        with open(CHAR_PATH / f'{char_id}.json', 'w', encoding='utf-8') as f:
            json.dump(char_map[char_id], f, ensure_ascii=False, indent=2)
