"""Developer Model"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.database import Base

class Developer(Base):
    """Developer Profile Model"""
    __tablename__ = "developer"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, unique=True)
    
    github_username = Column(String(100))
    gitlab_username = Column(String(100))
    linkedin_profile = Column(String(500))
    portfolio_url = Column(String(500))
    
    primary_language = Column(String(50))
    secondary_languages = Column(JSON, default=[])
    
    experience_years = Column(Integer)
    current_role = Column(String(100))
    company = Column(String(255))
    
    skills = Column(JSON, default=[])
    certifications = Column(JSON, default=[])
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

    # Relationships
    user = relationship("User", back_populates="developer")

    def __repr__(self):
        return f"<Developer {self.user_id}>"
