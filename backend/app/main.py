from fastapi import FastAPI
from app.database import engine, Base
from app.users import models
from app.users.router import router as users_router
from app.courses.router import router as courses_router


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users_router)
app.include_router(courses_router)