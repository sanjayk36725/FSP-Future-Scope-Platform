"""Student Model"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.database import Base

class Student(Base):
    """Student Profile Model"""
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, unique=True)
    
    roll_number = Column(String(50), unique=True, nullable=False)
    enrollment_number = Column(String(100), unique=True)
    
    department = Column(String(100))
    semester = Column(Integer)
    cgpa = Column(Numeric(3, 2), default=0.0)
    
    date_of_birth = Column(DateTime)
    address = Column(String(500))
    
    admission_date = Column(DateTime, default=datetime.utcnow)
    expected_graduation = Column(DateTime)
    
    parent_name = Column(String(100))
    parent_phone = Column(String(20))
    
    is_placed = Column(String(50), default="not_placed")  # not_placed, placed, rejected
    placed_company = Column(String(255))
    placed_package = Column(Numeric(10, 2))
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

    # Relationships
    user = relationship("User", back_populates="student")

    def __repr__(self):
        return f"<Student {self.roll_number}>"
