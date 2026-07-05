"""Notification Model"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.database import Base

class Notification(Base):
    """User Notification Model"""
    __tablename__ = "notification"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    
    title = Column(String(255), nullable=False)
    message = Column(String(1000), nullable=False)
    
    notification_type = Column(String(50))  # info, warning, error, success
    category = Column(String(100))  # placement, course, ai, system, etc.
    
    related_id = Column(Integer)  # ID of related entity
    related_type = Column(String(100))  # Type of related entity
    
    is_read = Column(Boolean, default=False)
    read_at = Column(DateTime, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="notifications")

    def __repr__(self):
        return f"<Notification {self.title}>"
