"""HR Employee Model"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.database import Base

class HREmployee(Base):
    """HR Employee Profile Model"""
    __tablename__ = "hr_employee"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, unique=True)
    company_id = Column(Integer, ForeignKey('company.id'))
    
    employee_id = Column(String(100), unique=True)
    designation = Column(String(100))
    department = Column(String(100))
    
    employee_count_responsible = Column(Integer)
    
    salary = Column(Numeric(12, 2))
    
    joining_date = Column(DateTime)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

    # Relationships
    user = relationship("User", back_populates="hr_employee")
    company = relationship("Company", back_populates="hr_employees")

    def __repr__(self):
        return f"<HREmployee {self.employee_id}>"
