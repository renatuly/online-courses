from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from .models import UserRole

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: UserRole = UserRole.STUDENT

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: UserRole
    created_at: datetime

    class Config:
        from_attributes = True # allows pydantic read the SQLAlchemy models