"""Audit and Activity Log Models"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON, Text
from datetime import datetime

from app.db.database import Base

class AuditLog(Base):
    """Audit Log for system operations"""
    __tablename__ = "audit_log"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    
    action = Column(String(100), nullable=False)
    entity_type = Column(String(100), nullable=False)
    entity_id = Column(Integer)
    
    old_values = Column(JSON, default={})
    new_values = Column(JSON, default={})
    
    ip_address = Column(String(50))
    user_agent = Column(String(500))
    
    status = Column(String(50), default="success")  # success, failed
    error_message = Column(Text, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<AuditLog {self.action}>"

class ActivityLog(Base):
    """Activity Log for user actions"""
    __tablename__ = "activity_log"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    
    activity_type = Column(String(100), nullable=False)  # login, upload, download, etc.
    description = Column(String(500))
    
    related_entity_type = Column(String(100))
    related_entity_id = Column(Integer)
    
    ip_address = Column(String(50))
    location = Column(String(255))
    device_type = Column(String(50))
    
    metadata = Column(JSON, default={})
    
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<ActivityLog {self.activity_type}>"
