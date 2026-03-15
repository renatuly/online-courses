from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from . import schemas, service, models
from app.courses.models import Course
from app.auth.dependencies import require_instructor

router = APIRouter(prefix="/sections", tags=["Sections"])

@router.post("/", response_model=schemas.SectionOut, status_code=status.HTTP_201_CREATED)
def create_section(
    section_data : schemas.SectionCreate,
    db: Session = Depends(get_db),
    current_user = Depends(require_instructor)
):
    return service.create_section(db,section_data, current_user.id)
