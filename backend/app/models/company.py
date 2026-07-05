"""Company Model"""

from sqlalchemy import Column, Integer, String, DateTime, Numeric, JSON
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.database import Base

class Company(Base):
    """Company Profile Model"""
    __tablename__ = "company"

    id = Column(Integer, primary_key=True, index=True)
    
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True)
    phone = Column(String(20))
    website = Column(String(500))
    
    industry = Column(String(100))
    company_size = Column(String(50))  # startup, small, medium, large, enterprise
    
    headquarters = Column(String(255))
    country = Column(String(100))
    
    description = Column(String(1000))
    logo_url = Column(String(500))
    
    founded_year = Column(Integer)
    annual_revenue = Column(Numeric(15, 2))
    employee_count = Column(Integer)
    
    is_verified = Column(String(50), default="pending")  # pending, verified, rejected
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

    # Relationships
    job_posts = relationship("JobPost", back_populates="company")
    recruiters = relationship("Recruiter", back_populates="company")
    hr_employees = relationship("HREmployee", back_populates="company")

    def __repr__(self):
        return f"<Company {self.name}>"
