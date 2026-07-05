"""File Service"""

from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
import os
import logging

from app.models.file import FileUpload
from app.utils import (
    validate_file_extension,
    validate_file_size,
    generate_unique_filename
)
from app.config import settings

logger = logging.getLogger(__name__)

class FileService:
    """File Service"""

    async def upload_file(self, file, user_id: int, db: Session) -> dict:
        """Upload and store file"""
        # Validate file
        if not file.filename:
            raise ValueError("No file provided")

        # Get file extension
        if '.' not in file.filename:
            raise ValueError("File must have an extension")
        
        ext = file.filename.rsplit('.', 1)[1].lower()
        if ext not in settings.ALLOWED_EXTENSIONS:
            raise ValueError(f"File type '.{ext}' is not allowed")

        # Read file content
        contents = await file.read()
        file_size = len(contents)

        # Validate file size
        if not validate_file_size(file_size, settings.MAX_FILE_SIZE):
            raise ValueError(f"File size exceeds maximum limit of {settings.MAX_FILE_SIZE / (1024*1024)} MB")

        # Create uploads directory if not exists
        os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

        # Generate unique filename
        unique_filename = generate_unique_filename(file.filename)
        file_path = os.path.join(settings.UPLOAD_DIR, unique_filename)

        # Save file
        with open(file_path, 'wb') as f:
            f.write(contents)

        # Save file metadata to database
        file_upload = FileUpload(
            user_id=user_id,
            original_filename=file.filename,
            stored_filename=unique_filename,
            file_path=file_path,
            file_type=ext,
            file_size=file_size,
            mime_type=file.content_type
        )
        db.add(file_upload)
        db.commit()
        db.refresh(file_upload)

        logger.info(f"File uploaded: {unique_filename} (User: {user_id})")

        return {
            "file_id": file_upload.id,
            "filename": unique_filename,
            "original_filename": file.filename,
            "file_size": file_size,
            "file_type": ext,
            "upload_date": file_upload.created_at.isoformat()
        }

    async def list_user_files(self, user_id: int, db: Session) -> List[FileUpload]:
        """List user's uploaded files"""
        files = db.query(FileUpload).filter(
            FileUpload.user_id == user_id,
            FileUpload.deleted_at.is_(None)
        ).order_by(FileUpload.created_at.desc()).all()
        return files

    async def get_file(self, file_id: int, user_id: int, db: Session) -> Optional[FileUpload]:
        """Get file details"""
        file = db.query(FileUpload).filter(
            FileUpload.id == file_id,
            FileUpload.user_id == user_id
        ).first()
        return file

    async def delete_file(self, file_id: int, user_id: int, db: Session):
        """Delete file (soft delete)"""
        file = db.query(FileUpload).filter(
            FileUpload.id == file_id,
            FileUpload.user_id == user_id
        ).first()
        
        if not file:
            raise ValueError("File not found")
        
        # Delete physical file
        if os.path.exists(file.file_path):
            os.remove(file.file_path)
        
        # Soft delete
        file.deleted_at = datetime.utcnow()
        db.commit()

        logger.info(f"File deleted: {file_id}")

    async def get_file_path(self, file_id: int, user_id: int, db: Session) -> Optional[str]:
        """Get file path for download"""
        file = await self.get_file(file_id, user_id, db)
        if file and os.path.exists(file.file_path):
            return file.file_path
        return None
