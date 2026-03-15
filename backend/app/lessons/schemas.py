from pydantic import BaseModel
from typing import Optional

class LessonCreate(BaseModel):
    title: str
    video_url : Optional[str] = None
    duration_seconds : int = 0
    order: int
    section_id : int

class LessonOut(LessonCreate):
    id : int

    class Config:
        from_attributes = True 