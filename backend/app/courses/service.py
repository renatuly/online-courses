from sqlalchemy.orm import Session
from . import models, schemas


def create_new_course(db: Session, course_data: schemas.CourseCreate, instructor_id: int):
    new_course = models.Course(
        **course_data.model_dump(), # the usage of '**' helps us to use all the information provided and map them into dictionary
        instructor_id = instructor_id
    )

    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return new_course
def get_all_courses(db:Session):
    return db.query(models.Course).filter(models.Course.is_published==True).all()

