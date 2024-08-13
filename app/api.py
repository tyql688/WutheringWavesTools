import json
from typing import Dict

import requests

from .RESOURCE_PATH import *

_session = requests.Session()


def download_all_character():
    res = _session.get('https://api.hakush.in/ww/data/character.json')
    res.raise_for_status()
    value = res.json()
    with open(RAW_CHARACTER_PATH, 'w', encoding='utf-8') as f:
        json.dump(value, f, ensure_ascii=False, indent=4)
    return value


def download_all_weapon():
    res = _session.get('https://api.hakush.in/ww/data/weapon.json')
    res.raise_for_status()
    value = res.json()
    with open(RAW_WEAPON_PATH, 'w', encoding='utf-8') as f:
        json.dump(value, f, ensure_ascii=False, indent=4)
    return value


def download_all_echo():
    res = _session.get('https://api.hakush.in/ww/data/echo.json')
    res.raise_for_status()
    value = res.json()
    with open(RAW_ECHO_PATH, 'w', encoding='utf-8') as f:
        json.dump(value, f, ensure_ascii=False, indent=4)
    return value


def download_all_detail(type: str, resource_id_list: list):
    for resource_id in resource_id_list:
        res = _session.get(f'https://api.hakush.in/ww/data/zh/{type}/{resource_id}.json')
        res.raise_for_status()
        with open(RAW_RESOURCE_PATH / f'{resource_id}.json', 'w', encoding='utf-8') as f:
            json.dump(res.json(), f, ensure_ascii=False, indent=4)


def download_all_avatar_pic(all_character: Dict, is_force: bool = False):
    for resource_id, temp in all_character.items():
        name = f'role_head_{resource_id}.png'
        path = AVATAR / name
        if not is_force and path.exists():
            continue
        resource_path = temp['icon'].split('.')[0].replace('/Game/Aki/', '')
        url = f'https://api.hakush.in/ww/{resource_path}.webp'
        res = _session.get(url)
        res.raise_for_status()
        with open(path, 'wb') as f:
            f.write(res.content)

    print(f'{len(all_character)} avatars downloaded')


def download_all_pile_pic(all_character: Dict, is_force: bool = False):
    for resource_id, _ in all_character.items():
        name = f'role_pile_{resource_id}.png'
        path = ROLE_PILE / name
        if not is_force and path.exists():
            continue
        with open(RAW_RESOURCE_PATH / f'{resource_id}.json', 'r', encoding='utf-8') as f:
            temp = json.load(f)
        resource_path = temp['Background'].split('.')[0].replace('/Game/Aki/', '')
        url = f'https://api.hakush.in/ww/{resource_path}.webp'
        res = _session.get(url)
        res.raise_for_status()
        with open(path, 'wb') as f:
            f.write(res.content)

    print(f'{len(all_character)} pile downloaded')


def download_all_weapon_pic(all_weapon: Dict, is_force: bool = False):
    for resource_id, temp in all_weapon.items():
        name = f'weapon_{resource_id}.png'
        path = WEAPON / name
        if not is_force and path.exists():
            continue
        resource_path = temp['icon'].split('.')[0].replace('/Game/Aki/', '')
        url = f'https://api.hakush.in/ww/{resource_path}.webp'
        res = _session.get(url)
        res.raise_for_status()
        with open(path, 'wb') as f:
            f.write(res.content)

    print(f'{len(all_weapon)} weapons downloaded')


def download():
    all_character = download_all_character()
    download_all_detail('character', all_character.keys())
    all_weapon = download_all_weapon()
    download_all_detail('weapon', all_weapon.keys())
    all_echo = download_all_echo()
    download_all_detail('echo', all_echo.keys())
    download_all_avatar_pic(all_character)
    download_all_pile_pic(all_character)
    download_all_weapon_pic(all_weapon)
