from pydantic import BaseModel
from typing import Optional

class SectionBase(BaseModel):
    title : str
    course_id : int
    order : int
class SectionCreate(SectionBase):
    pass
class SectionOut(SectionBase):
    id: int

    class Config:
        from_attributes = True