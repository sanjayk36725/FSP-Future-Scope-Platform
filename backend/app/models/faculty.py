"""Faculty Model"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.database import Base

class Faculty(Base):
    """Faculty Profile Model"""
    __tablename__ = "faculty"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, unique=True)
    
    employee_id = Column(String(50), unique=True, nullable=False)
    department = Column(String(100))
    designation = Column(String(100))
    specialization = Column(String(255))
    
    qualification = Column(String(255))
    experience_years = Column(Integer)
    
    office_room = Column(String(50))
    office_hours = Column(String(255))
    
    joining_date = Column(DateTime)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

    # Relationships
    user = relationship("User", back_populates="faculty")

    def __repr__(self):
        return f"<Faculty {self.employee_id}>"
