from fastapi import HTTPException, status
from sqlalchemy.orm import Session # you don't send just one thing you need manage group of things
from . import models, schemas
from app.courses.models import Course

def create_section(db: Session, section_data: schemas.SectionCreate, current_user_id : int):
    course = db.query(Course).filter(Course.id == section_data.course_id).first()
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Course with id {section_data.course_id} was not found ")

    if course.instructor.id != current_user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"This section does not belong to user {current_user_id}")

    new_section = models.Section(**section_data.model_dump())

    db.add(new_section)
    db.commit()
    db.refresh(new_section)

    return new_section