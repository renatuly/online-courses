from fastapi import APIRouter
from .schemas import UserCreate
router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def get_users():
    return {"message" : "list of users"}

@router.post("/")
def create_user(user: UserCreate):
    return {"message" : "user was created successfully"}