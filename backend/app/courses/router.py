from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from . import schemas, service
from app.users.models import User,UserRole

router = APIRouter(prefix="/courses", tags=["Courses"])

def get_current_instructor(db: Session = Depends(get_db)):
    user = db.query(User).filter(User.role == UserRole.INSTRUCTOR).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only instructors can perform this action"
        )
    return user


@router.post("/", response_model=schemas.CourseOut)
def create_course(
    course: schemas.CourseCreate,
    db: Session = Depends(get_db),
    instructor: User = Depends(get_current_instructor)
):
    return service.create_new_course(db,course,instructor.id)

@router.get("/",response_model=list[schemas.CourseOut])
def list_courses(db: Session = Depends(get_db)):
    return service.get_all_courses(db)
