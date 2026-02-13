from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional

from app.database import get_db
from app.models.course import Course
from app.auth.dependencies import get_current_user, require_instructor

router = APIRouter(prefix="/courses", tags=["Courses"])


@router.post("/")
def create_course(
    title: str,
    description: str,
    price: float,
    category: str,
    db: Session = Depends(get_db),
    instructor = Depends(require_instructor)
):
    course = Course(
        title=title,
        description=description,
        price=price,
        category=category,
        instructor_id=instructor.id
    )

    db.add(course)
    db.commit()
    db.refresh(course)

    return course


@router.get("/")
def list_courses(
    search: Optional[str] = None,
    category: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Course).filter(Course.is_published == True)

    if search:
        query = query.filter(Course.title.ilike(f"%{search}%"))

    if category:
        query = query.filter(Course.category == category)

    return query.all()


@router.get("/{course_id}")
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    return course


@router.patch("/{course_id}/publish")
def publish_course(
    course_id: int,
    db: Session = Depends(get_db),
    instructor = Depends(require_instructor)
):
    course = db.query(Course).filter(Course.id == course_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    if course.instructor_id != instructor.id:
        raise HTTPException(status_code=403, detail="Not your course")

    course.is_published = True
    db.commit()

    return {"message": "Course published"}
