from typing import Dict, List

from pydantic import BaseModel, Field, RootModel


class StatsDetail(BaseModel):
    Name: str
    Value: float
    IsRatio: bool
    IsPercent: bool


class WeaponStats(RootModel):
    root: Dict[str, List[StatsDetail]]


class Stats(RootModel):
    root: Dict[str, WeaponStats]


class AscensionMaterial(BaseModel):
    """突破材料项目"""
    key: int = Field(alias="Key")
    value: int = Field(alias="Value")


class WeaponModel(BaseModel):
    name: str = Field(alias="Name")
    starLevel: int = Field(alias="Rarity")
    type: int = Field(alias="Type")
    stats: Stats = Field(alias="Stats")
    effect: str = Field(alias="Effect")
    effectName: str = Field(alias="EffectName")
    param: List[List[str]] = Field(alias="Param")
    desc: str = Field(alias="Desc")
    ascensions: Dict[str, List[AscensionMaterial]] = Field(alias="Ascensions")
