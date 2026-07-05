"""Course Model"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric, JSON
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.database import Base

class Course(Base):
    """Course Model"""
    __tablename__ = "course"

    id = Column(Integer, primary_key=True, index=True)
    
    course_code = Column(String(50), unique=True, nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(String(1000))
    
    department = Column(String(100))
    semester = Column(Integer)
    
    credits = Column(Integer)
    total_hours = Column(Integer)
    
    faculty_id = Column(Integer, ForeignKey('faculty.id'))
    
    prerequisites = Column(JSON, default=[])
    learning_outcomes = Column(JSON, default=[])
    
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    
    max_students = Column(Integer)
    current_enrollment = Column(Integer, default=0)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"<Course {self.course_code}>"
