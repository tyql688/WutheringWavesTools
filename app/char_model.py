# 定义消耗资源的模型
from typing import List, Dict, Optional

from pydantic import BaseModel, Field, RootModel, field_validator

from app.utils import remove_text_inside_brackets


class SkillLevelDetail(BaseModel):
    Name: str
    Param: List[List[str]]


class SkillLevel(RootModel):
    root: SkillLevelDetail


class SkillDetail(BaseModel):
    Name: str
    Desc: str
    Param: List[str]
    Type: Optional[str] = None
    Level: Optional[Dict[str, SkillLevel]] = None

    @field_validator('Desc', mode='before')
    def clean_name(cls, v):
        return remove_text_inside_brackets(v)


class SkillNode(BaseModel):
    Skill: SkillDetail


class StatsDetail(BaseModel):
    Life: float
    Atk: float
    Def: float


class CharacterStats(RootModel):
    root: Dict[str, StatsDetail]


class Stats(RootModel):
    root: Dict[str, CharacterStats]


class ChainDetail(BaseModel):
    Name: str
    Desc: str
    Param: List[str]

    @field_validator('Desc', mode='before')
    def clean_name(cls, v):
        return remove_text_inside_brackets(v)


class Chains(RootModel):
    root: Dict[str, ChainDetail]


class AscensionMaterial(BaseModel):
    """突破材料项目"""
    key: int = Field(alias="Key")
    value: int = Field(alias="Value")


# 定义模型
class CharModel(BaseModel):
    name: str = Field(alias="Name")
    attributeId: int = Field(alias="Element")
    weaponTypeId: int = Field(alias="Weapon")
    starLevel: int = Field(alias="Rarity")
    stats: Stats = Field(alias="Stats")
    # levelExp: List[int] = Field(alias="LevelEXP")
    skillTree: Dict[str, SkillNode] = Field(alias="SkillTrees")
    chains: Chains = Field(alias="Chains")
    ascensions: Dict[str, List[AscensionMaterial]] = Field(alias="Ascensions")
