from fastapi import FastAPI
from app.database import engine, Base
from app.models import User
from app.routers import auth, courses

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(courses.router)




@app.get("/")
def root():
    return {"message": "Online Learning Platform API is running"}
