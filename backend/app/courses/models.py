import enum
from sqlalchemy import Column, BigInteger, Text, Enum, Boolean, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from app.database import Base

class CourseCategory(str, enum.Enum):
    DEVELOPMENT = "development"
    BUSINESS = "business"
    DESIGN = "design"
    MARKETING = "marketing"

class Course(Base):
    __tablename__ = "courses"

    id = Column(BigInteger, primary_key=True, index=True)
    title = Column(Text, nullable=False)
    description = Column(Text)
    price = Column(BigInteger, default=0) 
    category = Column(Enum(CourseCategory))
    thumbnail_url = Column(Text)
    instructor_id = Column(BigInteger, ForeignKey("users.id"))
    is_published = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationship back to the User model
    instructor = relationship("User")