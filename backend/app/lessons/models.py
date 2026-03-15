from sqlalchemy import Column, BigInteger, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Lesson(Base):
    __tablename__ = "lessons"
    id = Column(BigInteger,primary_key=True,index = True)
    title = Column(Text, nullable=False)
    video_url = Column(Text, nullable=True)
    duration_seconds = Column(BigInteger,default=0)
    order = Column(BigInteger,index=True)
    section_id = Column(BigInteger,ForeignKey("sections.id"), nullable=False)
    section = relationship("Section")

