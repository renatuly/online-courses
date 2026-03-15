from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from . import models, schemas
from app.sections.models import Section

def create_lesson(db:Session, lesson_data : schemas.LessonCreate, current_user_id : int):
    section = db.query(Section).filter(Section.id == lesson_data.section_id).first()

    if not section:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Section not found")

    if section.course.instructor_id !=current_user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Current user is not allowed")
    
    new_lesson = models.Lesson(**lesson_data.model_dump())
    db.add(new_lesson)
    db.commit()
    db.refresh(new_lesson)

    return new_lesson