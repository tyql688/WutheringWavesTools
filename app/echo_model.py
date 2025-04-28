from typing import Dict, List, Any

from pydantic import BaseModel, Field, RootModel, field_validator

from app.utils import remove_text_inside_brackets


class GroupDetail(BaseModel):
    # id: int = Field(alias="Id")
    Name: str = Field(alias="Name")
    # Set: Dict[str, Any]


class GroupNode(RootModel):
    root: Dict[str, GroupDetail]


class SkillNode(BaseModel):
    desc: str = Field(alias="Desc")
    simpleDesc: str = Field(alias="SimpleDesc")
    params: List[Any] = Field(alias="Param")

    @field_validator("desc", mode="before")
    def clean_desc_name(cls, v):
        return remove_text_inside_brackets(v)

    @field_validator("simpleDesc", mode="before")
    def clean_simpleDesc_name(cls, v):
        return remove_text_inside_brackets(v)


class EchoModel(BaseModel):
    id: int = Field(alias="Id")
    name: str = Field(alias="Name")
    # starLevel: List = Field(alias="Rarity")
    intensityCode: int = Field(alias="IntensityCode")  # 0:c1 , 1:c3 , 2:c4
    group: GroupNode = Field(alias="Group")
    skill: SkillNode = Field(alias="Skill")
