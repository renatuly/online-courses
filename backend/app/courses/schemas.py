from pydantic import BaseModel
from typing import Optional
from .models import CourseCategory

class CourseCreate(BaseModel):
    title: str
    description: Optional[str] = None
    price: int
    category: CourseCategory
    thumbnail_url: Optional[str] = None

class CourseOut(CourseCreate):
    id: int
    instructor_id: int
    is_published: bool

    class Config:
        from_attributes = True