"""Resume Model"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric, JSON
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.database import Base

class Resume(Base):
    """Resume Model"""
    __tablename__ = "resume"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    
    title = Column(String(255))
    file_path = Column(String(500), nullable=False)
    file_size = Column(Integer)  # in bytes
    
    summary = Column(String(1000))
    skills = Column(JSON, default=[])
    
    experience = Column(JSON, default=[])
    education = Column(JSON, default=[])
    certifications = Column(JSON, default=[])
    projects = Column(JSON, default=[])
    
    ats_score = Column(Numeric(3, 2), default=0)  # 0-100
    ai_feedback = Column(String(2000))
    
    is_primary = Column(String(50), default="no")  # yes, no
    version = Column(Integer, default=1)
    
    last_reviewed_at = Column(DateTime)
    reviewed_by_ai_at = Column(DateTime)
    
    is_active = Column(String(50), default="yes")
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

    # Relationships
    user = relationship("User")

    def __repr__(self):
        return f"<Resume {self.title}>"
