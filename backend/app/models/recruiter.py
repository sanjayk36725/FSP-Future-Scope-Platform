"""Recruiter Model"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.database import Base

class Recruiter(Base):
    """Recruiter Profile Model"""
    __tablename__ = "recruiter"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, unique=True)
    company_id = Column(Integer, ForeignKey('company.id'))
    
    employee_id = Column(String(100), unique=True)
    designation = Column(String(100))
    department = Column(String(100))
    
    linkedin_url = Column(String(500))
    
    hiring_budget = Column(Numeric(15, 2))
    positions_to_fill = Column(Integer)
    
    experience_in_recruitment = Column(Integer)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

    # Relationships
    user = relationship("User", back_populates="recruiter")
    company = relationship("Company", back_populates="recruiters")

    def __repr__(self):
        return f"<Recruiter {self.employee_id}>"
