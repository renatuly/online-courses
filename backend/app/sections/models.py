from sqlalchemy import Column, BigInteger, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Section(Base):
    __tablename__ = "sections"

    id = Column(BigInteger,primary_key=True,index=True)
    title = Column(Text, nullable=False)
    order = Column(BigInteger,index= True)
    course_id = Column(BigInteger,ForeignKey("courses.id"),nullable = False)
    course = relationship("Course")