"""File Upload Model"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.database import Base

class FileUpload(Base):
    """File Upload Model"""
    __tablename__ = "file_upload"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    
    original_filename = Column(String(500), nullable=False)
    stored_filename = Column(String(500), nullable=False)
    file_path = Column(String(1000), nullable=False)
    
    file_type = Column(String(50))  # pdf, docx, txt, csv, xlsx, jpg, png, etc.
    file_size = Column(BigInteger)  # in bytes
    
    mime_type = Column(String(100))
    
    is_public = Column(String(50), default="no")
    
    description = Column(String(500))
    tags = Column(String(500))
    
    upload_ip = Column(String(50))
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

    # Relationships
    user = relationship("User", back_populates="uploaded_files")

    def __repr__(self):
        return f"<FileUpload {self.original_filename}>"
