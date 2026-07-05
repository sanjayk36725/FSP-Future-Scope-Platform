"""Administrator Model"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.database import Base

class Administrator(Base):
    """Administrator Profile Model"""
    __tablename__ = "administrator"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, unique=True)
    
    employee_id = Column(String(100), unique=True)
    department = Column(String(100))
    
    access_level = Column(String(50), default="standard")  # standard, advanced, full
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

    # Relationships
    user = relationship("User", back_populates="administrator")

    def __repr__(self):
        return f"<Administrator {self.employee_id}>"
