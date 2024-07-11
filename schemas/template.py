from typing import List, Optional
from pydantic import BaseModel


class Field(BaseModel):
    field_name: str
    field_rename: str
    field_type: str
    field_is_active: bool


class Section(BaseModel):
    section_name: str
    section_rename: str
    section_is_active: bool
    section_fields: List[Field]


class Tab(BaseModel):
    tab_name: str
    tab_rename: str
    tab_is_active: bool
    tab_sections: Optional[List[Section]] = None


class Template(BaseModel):
    name: str
    rename: str
    tabs: List[Tab]
