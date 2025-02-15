from pathlib import Path

MAIN_PATH = Path(__file__).parents[1] / 'resource'

ROLE = MAIN_PATH / 'role'

PIC = MAIN_PATH / 'pic'
WEAPON = PIC / 'weapon'
PHANTOM = PIC / 'phantom'
ITEM = PIC / 'item'
MATERIAL = PIC / 'material'
AVATAR = PIC / 'avatar'
ROLE_PILE = PIC / 'role_pile'
ROLE_DETAIL_SKILL_PATH = PIC / 'skill'
ROLE_DETAIL_CHAINS_PATH = PIC / 'chains'
SELF_PATH = PIC / 'self'
ATTRIBUTE_EFFECT_PATH = PIC / 'attribute_effect'
CHARACTER_MAP_PATH = MAIN_PATH / 'resource.json'
CHAR_ID_PATH = MAIN_PATH / 'CharId2Data.json'
CHAR_ALIAS_PATH = MAIN_PATH / 'char_alias.json'
# CHAR_PATH = MAIN_PATH / 'charData.json'
# WEAPON_PATH = MAIN_PATH / 'weaponData.json'
CHAR_PATH = MAIN_PATH / 'detail_json/char'
WEAPON_PATH = MAIN_PATH / 'detail_json/weapon'
MATERIAL_PATH = MAIN_PATH / 'detail_json/material'

WEAPON_ALIAS_PATH = MAIN_PATH / 'weapon_alias.json'

ID_NAME_PATH = MAIN_PATH / 'id2name.json'

RAW_DATA_PATH = MAIN_PATH / 'raw'
RAW_RESOURCE_PATH = RAW_DATA_PATH / 'resource'
RAW_CHARACTER_PATH = RAW_DATA_PATH / 'character.json'
RAW_WEAPON_PATH = RAW_DATA_PATH / 'weapon.json'
RAW_ECHO_PATH = RAW_DATA_PATH / 'echo.json'
RAW_ITEM_PATH = RAW_DATA_PATH / 'item.json'

APP_PATH = Path(__file__).parents[1] / 'app'

MATERIAL_TAG = ["共鸣者突破材料", "突破材料", "武器与技能素材", "技能升级材料", "突破材料", "通用货币",
                "共鸣者经验材料", "武器经验材料"]


def init_dir():
    for i in [
        MAIN_PATH,
        ROLE,
        ROLE_DETAIL_SKILL_PATH,
        ROLE_DETAIL_CHAINS_PATH,
        PIC,
        WEAPON,
        PHANTOM,
        AVATAR,
        ROLE_PILE,
        RAW_DATA_PATH,
        RAW_RESOURCE_PATH
    ]:
        i.mkdir(parents=True, exist_ok=True)


init_dir()
