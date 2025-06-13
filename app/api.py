import asyncio
import json
import shutil
from typing import Dict

import aiofiles
import aiohttp
import requests

from app.RESOURCE_PATH import (
    AVATAR,
    ITEM,
    MATERIAL,
    MATERIAL_TAG,
    PHANTOM,
    RAW_CHARACTER_PATH,
    RAW_ECHO_PATH,
    RAW_ITEM_PATH,
    RAW_RESOURCE_PATH,
    RAW_WEAPON_PATH,
    ROLE_DETAIL_CHAINS_PATH,
    ROLE_DETAIL_SKILL_PATH,
    ROLE_PILE,
    SELF_PATH,
    WEAPON,
)

# 保留同步会话用于兼容性
_session = requests.Session()

# 异步会话将在异步函数中创建


async def async_download_all_character(session: aiohttp.ClientSession) -> Dict:
    """异步下载所有角色数据"""
    async with session.get("https://api.hakush.in/ww/data/character.json") as res:
        res.raise_for_status()
        value = await res.json()
        async with aiofiles.open(RAW_CHARACTER_PATH, "w", encoding="utf-8") as f:
            await f.write(json.dumps(value, ensure_ascii=False, indent=4))
        return value


async def async_download_all_weapon(session: aiohttp.ClientSession) -> Dict:
    """异步下载所有武器数据"""
    async with session.get("https://api.hakush.in/ww/data/weapon.json") as res:
        res.raise_for_status()
        value = await res.json()
        async with aiofiles.open(RAW_WEAPON_PATH, "w", encoding="utf-8") as f:
            await f.write(json.dumps(value, ensure_ascii=False, indent=4))
        return value


async def async_download_all_echo(session: aiohttp.ClientSession) -> Dict:
    """异步下载所有声骸数据"""
    async with session.get("https://api.hakush.in/ww/data/echo.json") as res:
        res.raise_for_status()
        value = await res.json()
        async with aiofiles.open(RAW_ECHO_PATH, "w", encoding="utf-8") as f:
            await f.write(json.dumps(value, ensure_ascii=False, indent=4))
        return value


async def async_download_all_detail(
    session: aiohttp.ClientSession, type: str, resource_id_list: list
):
    """异步下载所有详细数据"""

    async def download_one(resource_id):
        url = f"https://api.hakush.in/ww/data/zh/{type}/{resource_id}.json"
        async with session.get(url) as res:
            res.raise_for_status()
            data = await res.json()
            file_path = RAW_RESOURCE_PATH / f"{resource_id}.json"
            async with aiofiles.open(file_path, "w", encoding="utf-8") as f:
                await f.write(json.dumps(data, ensure_ascii=False, indent=4))

    # 使用asyncio.gather并发下载所有资源
    await asyncio.gather(
        *[download_one(resource_id) for resource_id in resource_id_list]
    )


async def async_download_all_item(session: aiohttp.ClientSession) -> Dict:
    """异步下载所有物品数据"""
    async with session.get("https://api.hakush.in/ww/data/zh/item.json") as res:
        res.raise_for_status()
        value = await res.json()
        async with aiofiles.open(RAW_ITEM_PATH, "w", encoding="utf-8") as f:
            await f.write(json.dumps(value, ensure_ascii=False, indent=4))
        return value


async def async_download_all_avatar_pic(
    session: aiohttp.ClientSession, all_character: Dict, is_force: bool = False
):
    """异步下载所有角色头像"""

    async def download_one(resource_id, temp):
        name = f"role_head_{resource_id}.png"
        path = AVATAR / name
        if not is_force and path.exists():
            return
        resource_path = temp["icon"].split(".")[0].replace("/Game/Aki/", "")
        url = f"https://api.hakush.in/ww/{resource_path}.webp"
        try:
            async with session.get(url) as res:
                res.raise_for_status()
                content = await res.read()
                async with aiofiles.open(path, "wb") as f:
                    await f.write(content)
        except Exception as _:
            pass

    # 使用asyncio.gather并发下载所有头像
    await asyncio.gather(
        *[
            download_one(resource_id, temp)
            for resource_id, temp in all_character.items()
        ]
    )
    print(f"{len(all_character)} avatars downloaded")


async def async_download_all_pile_pic(
    session: aiohttp.ClientSession, all_character: Dict, is_force: bool = False
):
    """异步下载所有角色立绘"""

    async def download_one(resource_id):
        name = f"role_pile_{resource_id}.png"
        path = ROLE_PILE / name
        if not is_force and path.exists():
            return
        try:
            async with aiofiles.open(
                RAW_RESOURCE_PATH / f"{resource_id}.json", "r", encoding="utf-8"
            ) as f:
                temp = json.loads(await f.read())
            resource_path = temp["Background"].split(".")[0].replace("/Game/Aki/", "")
            url = f"https://api.hakush.in/ww/{resource_path}.webp"
            async with session.get(url) as res:
                res.raise_for_status()
                content = await res.read()
                async with aiofiles.open(path, "wb") as f:
                    await f.write(content)
        except Exception as _:
            pass

    # 使用asyncio.gather并发下载所有立绘
    await asyncio.gather(
        *[download_one(resource_id) for resource_id in all_character.keys()]
    )
    print(f"{len(all_character)} pile downloaded")


async def async_download_all_weapon_pic(
    session: aiohttp.ClientSession, all_weapon: Dict, is_force: bool = False
):
    """异步下载所有武器图片"""

    async def download_one(resource_id, temp):
        name = f"weapon_{resource_id}.png"
        path = WEAPON / name
        if not is_force and path.exists():
            return
        try:
            resource_path = temp["icon"].split(".")[0].replace("/Game/Aki/", "")
            url = f"https://api.hakush.in/ww/{resource_path}.webp"
            async with session.get(url) as res:
                res.raise_for_status()
                content = await res.read()
                async with aiofiles.open(path, "wb") as f:
                    await f.write(content)
        except Exception:
            pass

    # 使用asyncio.gather并发下载所有武器图片
    await asyncio.gather(
        *[download_one(resource_id, temp) for resource_id, temp in all_weapon.items()]
    )
    print(f"{len(all_weapon)} weapons downloaded")


async def async_download_all_phantom_pic(
    session: aiohttp.ClientSession, all_echo: Dict, is_force: bool = False
):
    """异步下载所有声骸图片"""

    async def download_one(resource_id, temp):
        name = f"phantom_{resource_id}.png"
        path = PHANTOM / name
        if not is_force and path.exists():
            return
        try:
            resource_path = temp["icon"].split(".")[0].replace("/Game/Aki/", "")
            url = f"https://api.hakush.in/ww/{resource_path}.webp"
            async with session.get(url) as res:
                res.raise_for_status()
                content = await res.read()
                async with aiofiles.open(path, "wb") as f:
                    await f.write(content)
        except Exception:
            pass

    # 使用asyncio.gather并发下载所有声骸图片
    await asyncio.gather(
        *[download_one(resource_id, temp) for resource_id, temp in all_echo.items()]
    )
    print(f"{len(all_echo)} echoes downloaded")


async def async_download_all_item_pic(
    session: aiohttp.ClientSession, all_items: Dict, is_force: bool = False
):
    """异步下载所有物品图片"""
    if is_force:
        shutil.rmtree(ITEM, ignore_errors=True)
        ITEM.mkdir(parents=True, exist_ok=True)

    async def download_one(resource_id, temp):
        name = f"item_{resource_id}.png"
        path = ITEM / name
        if not is_force and path.exists():
            return
        try:
            resource_path = temp["icon"].split(".")[0].replace("/Game/Aki/", "")
            url = f"https://api.hakush.in/ww/{resource_path}.webp"
            async with session.get(url) as res:
                res.raise_for_status()
                content = await res.read()
                async with aiofiles.open(path, "wb") as f:
                    await f.write(content)
        except Exception:
            pass

    # 使用asyncio.gather并发下载所有物品图片
    await asyncio.gather(
        *[download_one(resource_id, temp) for resource_id, temp in all_items.items()]
    )
    print(f"{len(all_items)} items downloaded")


async def async_download_all_material_pic(
    session: aiohttp.ClientSession, all_items: Dict, is_force: bool = False
):
    """异步下载所有材料图片"""
    # 删除MATERIAL目录
    if is_force:
        shutil.rmtree(MATERIAL, ignore_errors=True)
        MATERIAL.mkdir(parents=True, exist_ok=True)

    count = 0

    async def download_one(resource_id, temp):
        nonlocal count
        if "tag" not in temp:
            return
        if temp["tag"][0] not in MATERIAL_TAG:
            return
        count += 1
        name = f"material_{resource_id}.png"
        path = MATERIAL / name
        if not is_force and path.exists():
            return
        try:
            resource_path = temp["icon"].split(".")[0].replace("/Game/Aki/", "")
            url = f"https://api.hakush.in/ww/{resource_path}.webp"
            async with session.get(url) as res:
                res.raise_for_status()
                content = await res.read()
                async with aiofiles.open(path, "wb") as f:
                    await f.write(content)
        except Exception:
            pass

    # 使用asyncio.gather并发下载所有材料图片
    await asyncio.gather(
        *[download_one(resource_id, temp) for resource_id, temp in all_items.items()]
    )
    print(f"{count} 突破材料 downloaded")


async def async_download_skill_pic(
    session: aiohttp.ClientSession, all_character: Dict, is_force: bool = False
):
    """异步下载所有技能图片"""
    if is_force:
        shutil.rmtree(ROLE_DETAIL_SKILL_PATH, ignore_errors=True)
        ROLE_DETAIL_SKILL_PATH.mkdir(parents=True, exist_ok=True)

    async def download_character_skills(resource_id):
        _dir = ROLE_DETAIL_SKILL_PATH / resource_id
        _dir.mkdir(parents=True, exist_ok=True)

        try:
            async with aiofiles.open(
                f"{RAW_RESOURCE_PATH}/{resource_id}.json", "r", encoding="utf-8"
            ) as f:
                role_detail = json.loads(await f.read())

            skill_tree = role_detail["SkillTrees"]
            download_tasks = []
            for skill_id, skill in skill_tree.items():
                name = f'skill_{skill["Skill"]["Name"]}.png'
                path = _dir / name
                if not is_force and path.exists():
                    continue

                download_tasks.append(download_one_skill(skill_id, skill, path))

            await asyncio.gather(*download_tasks)
        except Exception as e:
            print(f"Error processing character {resource_id}: {e}")

    async def download_one_skill(skill_id, skill, path):
        try:
            resource_path = (
                skill["Skill"]["Icon"].split(".")[0].replace("/Game/Aki/", "")
            )
            url = f"https://api.hakush.in/ww/{resource_path}.webp"

            async with session.get(url) as res:
                res.raise_for_status()
                content = await res.read()
                async with aiofiles.open(path, "wb") as f:
                    await f.write(content)
        except Exception:
            pass

    # 使用asyncio.gather并发下载所有角色的技能图片
    await asyncio.gather(
        *[
            download_character_skills(resource_id)
            for resource_id in all_character.keys()
        ]
    )
    print(f"{len(all_character)} skill downloaded")


async def async_download_chain_pic(
    session: aiohttp.ClientSession, all_character: Dict, is_force: bool = False
):
    """异步下载所有连携图片"""
    if is_force:
        shutil.rmtree(ROLE_DETAIL_CHAINS_PATH, ignore_errors=True)
        ROLE_DETAIL_CHAINS_PATH.mkdir(parents=True, exist_ok=True)

    async def download_character_chains(resource_id):
        _dir = ROLE_DETAIL_CHAINS_PATH / resource_id
        _dir.mkdir(parents=True, exist_ok=True)

        try:
            async with aiofiles.open(
                f"{RAW_RESOURCE_PATH}/{resource_id}.json", "r", encoding="utf-8"
            ) as f:
                role_detail = json.loads(await f.read())

            chains = role_detail["Chains"]
            download_tasks = []
            for chain_id, chain in chains.items():
                name = f"chain_{chain_id}.png"
                path = _dir / name
                if not is_force and path.exists():
                    continue

                download_tasks.append(download_one_chain(chain_id, chain, path))

            await asyncio.gather(*download_tasks)
        except Exception as e:
            print(f"Error processing character {resource_id}: {e}")

    async def download_one_chain(chain_id, chain, path):
        try:
            resource_path = chain["Icon"].split(".")[0].replace("/Game/Aki/", "")
            url = f"https://api.hakush.in/ww/{resource_path}.webp"

            async with session.get(url) as res:
                res.raise_for_status()
                content = await res.read()
                async with aiofiles.open(path, "wb") as f:
                    await f.write(content)
        except Exception:
            pass

    # 使用asyncio.gather并发下载所有角色的连携图片
    await asyncio.gather(
        *[
            download_character_chains(resource_id)
            for resource_id in all_character.keys()
        ]
    )
    print(f"{len(all_character)} chain downloaded")


async def async_download_url(url_list, self_path=SELF_PATH):
    """异步下载URL列表"""

    # 创建异步会话
    async with aiohttp.ClientSession() as session:

        async def download_one(name, url):
            path = self_path / name
            try:
                async with session.get(url) as res:
                    res.raise_for_status()
                    content = await res.read()
                    async with aiofiles.open(path, "wb") as f:
                        await f.write(content)
            except Exception:
                pass

        # 使用asyncio.gather并发下载所有URL
        await asyncio.gather(
            *[download_one(name, url) for name, url in url_list.items()]
        )
        print(f"{len(url_list)} urls downloaded")


async def async_download():
    """异步下载所有资源"""
    # 创建异步会话
    async with aiohttp.ClientSession() as session:
        # 获取所有数据
        all_character = await async_download_all_character(session)
        await async_download_all_detail(
            session, "character", list(all_character.keys())
        )
        all_weapon = await async_download_all_weapon(session)
        await async_download_all_detail(session, "weapon", list(all_weapon.keys()))
        all_echo = await async_download_all_echo(session)
        await async_download_all_detail(session, "echo", list(all_echo.keys()))
        all_item = await async_download_all_item(session)
        await async_download_all_detail(session, "item", list(all_item.keys()))

        # 并行下载所有图片资源
        await asyncio.gather(
            async_download_all_avatar_pic(session, all_character),
            async_download_all_pile_pic(session, all_character),
            async_download_all_weapon_pic(session, all_weapon),
            async_download_all_phantom_pic(session, all_echo),
            async_download_all_item_pic(session, all_item),
            async_download_all_material_pic(session, all_item),
            async_download_skill_pic(session, all_character),
            async_download_chain_pic(session, all_character),
        )

        print("所有资源下载完成！")
