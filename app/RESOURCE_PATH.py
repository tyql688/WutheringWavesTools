from pathlib import Path

MAIN_PATH = Path(__file__).parents[1] / 'resource'

ROLE = MAIN_PATH / 'role'
PIC = MAIN_PATH / 'pic'
WEAPON = PIC / 'weapon'
AVATAR = PIC / 'avatar'
ROLE_PILE = PIC / 'role_pile'
CHARACTER_MAP_PATH = MAIN_PATH / 'resource.json'
ID_NAME_PATH = MAIN_PATH / 'id2name.json'
NAME_ID_PATH = MAIN_PATH / 'name2id.json'

RAW_DATA_PATH = MAIN_PATH / 'raw'
RAW_RESOURCE_PATH = RAW_DATA_PATH / 'resource'
RAW_CHARACTER_PATH = RAW_DATA_PATH / 'character.json'
RAW_WEAPON_PATH = RAW_DATA_PATH / 'weapon.json'
RAW_ECHO_PATH = RAW_DATA_PATH / 'echo.json'


def init_dir():
    for i in [
        MAIN_PATH,
        ROLE,
        PIC,
        WEAPON,
        AVATAR,
        ROLE_PILE,
        RAW_DATA_PATH,
        RAW_RESOURCE_PATH
    ]:
        i.mkdir(parents=True, exist_ok=True)


init_dir()
