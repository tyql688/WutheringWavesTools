import json

from app.RESOURCE_PATH import RAW_WEAPON_PATH, RAW_RESOURCE_PATH, APP_PATH, RAW_ECHO_PATH, RAW_CHARACTER_PATH
from app.utils import lower_first_letter
from app.weapon_model import WeaponModel


def generate_model(cls_name, weapon_id, weapon_type, weapon_name):
    return f"""
class {cls_name}(WeaponAbstract):
    id = {weapon_id}
    type = {weapon_type}
    name = "{weapon_name}"
    """


def generate_weapon():
    weapon_map = {}
    with open(RAW_WEAPON_PATH, 'r', encoding='utf-8') as f:
        all_weapon = json.load(f)
        all_weapon = dict(sorted(all_weapon.items()))

        for weapon_id in all_weapon.keys():
            with open(f"{RAW_RESOURCE_PATH}/{weapon_id}.json", 'r', encoding='utf-8') as f:
                weapon_detail = json.load(f)

            weapon_detail = WeaponModel.parse_obj(weapon_detail)
            weapon_map[weapon_id] = lower_first_letter(weapon_detail.dict(exclude_none=True))

    with open(APP_PATH / "abstract/generate_weapon.py", 'w', encoding='utf-8') as f:
        f.write("from app.abstract.abstract import WavesWeaponRegister")
        f.write("\n")
        f.write("from app.abstract.abstract_weapon import WeaponAbstract")
        f.write("\n\n")
        for weapon_id, weapon_detail in weapon_map.items():
            cls_name = f"Weapon_{weapon_id}"
            weapon_class = generate_model(cls_name, weapon_id, weapon_detail['type'], weapon_detail['name'])
            f.write(weapon_class)
            f.write("\n")

        f.write("\n")
        for weapon_id, weapon_detail in weapon_map.items():
            cls_name = f"Weapon_{weapon_id}"
            f.write(f"WavesWeaponRegister.register_class({cls_name}.id, {cls_name})")
            f.write("\n")


def generate_echo_model(cls_name, echo_id, echo_name):
    return f"""
class {cls_name}(EchoAbstract):
    id = {echo_id}
    name = "{echo_name}"
    """


def generate_echo():
    echo_map = {}
    with open(RAW_ECHO_PATH, 'r', encoding='utf-8') as f:
        all_echo = json.load(f)
        all_echo = dict(sorted(all_echo.items()))

        for echo_id in all_echo.keys():
            with open(f"{RAW_RESOURCE_PATH}/{echo_id}.json", 'r', encoding='utf-8') as f:
                echo_detail = json.load(f)

            echo_map[echo_id] = {
                "id": echo_id,
                "name": echo_detail['Name']
            }

    with open(APP_PATH / "abstract/generate_echo.py", 'w', encoding='utf-8') as f:
        f.write("from app.abstract.abstract import WavesEchoRegister")
        f.write("\n")
        f.write("from app.abstract.abstract_echo import EchoAbstract")
        f.write("\n\n")
        for echo_id, echo_detail in echo_map.items():
            cls_name = f"Echo_{echo_id}"
            weapon_class = generate_echo_model(cls_name, echo_id, echo_detail['name'])
            f.write(weapon_class)
            f.write("\n")

        f.write("\n")
        for echo_id, echo_detail in echo_map.items():
            cls_name = f"Echo_{echo_id}"
            f.write(f"WavesEchoRegister.register_class({cls_name}.id, {cls_name})")
            f.write("\n")


def generate_char_model(cls_name, char_id, char_name, starLevel):
    return f"""
class {cls_name}(CharAbstract):
    id = {char_id}
    name = "{char_name}"
    starLevel = {starLevel}
    """


def generate_char():
    char_map = {}
    with open(RAW_CHARACTER_PATH, 'r', encoding='utf-8') as f:
        all_char = json.load(f)
        all_char = dict(sorted(all_char.items()))

        for char_id in all_char.keys():
            with open(f"{RAW_RESOURCE_PATH}/{char_id}.json", 'r', encoding='utf-8') as f:
                char_detail = json.load(f)

            char_map[char_id] = {
                "id": char_id,
                "name": char_detail['Name'],
                "starLevel": char_detail['Rarity']
            }

    with open(APP_PATH / "abstract/generate_char.py", 'w', encoding='utf-8') as f:
        f.write("from app.abstract.abstract import WavesCharRegister")
        f.write("\n")
        f.write("from app.abstract.abstract_char import CharAbstract")
        f.write("\n\n")
        for char_id, char_detail in char_map.items():
            cls_name = f"Char_{char_id}"
            weapon_class = generate_char_model(cls_name, char_id, char_detail['name'], char_detail['starLevel'])
            f.write(weapon_class)
            f.write("\n")

        f.write("\n")
        for char_id, char_detail in char_map.items():
            cls_name = f"Char_{char_id}"
            f.write(f"WavesCharRegister.register_class({cls_name}.id, {cls_name})")
            f.write("\n")
