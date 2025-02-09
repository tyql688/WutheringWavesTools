from typing import List

from pydantic import BaseModel, Field


class MaterialItem(BaseModel):
    id: int = Field(alias="Id")
    rarity: int = Field(alias="Rarity")
    type: int = Field(alias="Type")
    tag_num: List[int] = Field(alias="TagNum")
    name: str = Field(alias="Name")
    desc: str = Field(alias="Desc")
    bg: str = Field(alias="Bg")
    source: List[str] = Field(alias="Source")

    class Config:
        populate_by_name = True


# 使用示例
if __name__ == "__main__":
    item_data = {
        "Id": 41400154,
        "Rarity": 4,
        "Type": 4,
        "Tag": ["共鸣者突破材料"],
        "TagNum": [7],
        "Name": "幽囚拓扑",
        "Desc": "无归的谬误的掉落物，用于共鸣者突破。",
        "Bg": "无止无休的数据拓扑，也是维系永恒与无限的纽带。泰缇斯系统以因果织造囚笼，将未明的变量拘束其中——不论爱或希望。",
        "Icon": "/Game/Aki/UI/UIResources/Common/Image/IconMout/T_IconMout_L_015_UI.T_IconMout_L_015_UI",
        "Source": ["无归的谬误挑战获得"]
    }

    item = GameItem.model_validate(item_data)
    print(f"物品名称: {item.name}")
    print(f"稀有度: {item.rarity}")
    print(f"类型: {item.type}")
