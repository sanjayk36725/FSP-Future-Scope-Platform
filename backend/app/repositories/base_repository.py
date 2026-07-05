"""Repository Base Class"""

from sqlalchemy.orm import Session
from typing import TypeVar, Generic, Optional, List
from datetime import datetime

T = TypeVar('T')

class BaseRepository(Generic[T]):
    """Base repository for database operations"""

    def __init__(self, model: T, db: Session):
        self.model = model
        self.db = db

    def create(self, obj_in) -> T:
        """Create new record"""
        db_obj = self.model(**obj_in.dict())
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def get_by_id(self, obj_id: int) -> Optional[T]:
        """Get record by ID"""
        return self.db.query(self.model).filter(self.model.id == obj_id).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        """Get all records"""
        return self.db.query(self.model).offset(skip).limit(limit).all()

    def update(self, obj_id: int, obj_in) -> Optional[T]:
        """Update record"""
        db_obj = self.get_by_id(obj_id)
        if db_obj:
            for field, value in obj_in.dict(exclude_unset=True).items():
                setattr(db_obj, field, value)
            self.db.commit()
            self.db.refresh(db_obj)
        return db_obj

    def delete(self, obj_id: int) -> bool:
        """Delete record"""
        db_obj = self.get_by_id(obj_id)
        if db_obj:
            self.db.delete(db_obj)
            self.db.commit()
            return True
        return False

    def soft_delete(self, obj_id: int) -> bool:
        """Soft delete record"""
        db_obj = self.get_by_id(obj_id)
        if db_obj and hasattr(db_obj, 'deleted_at'):
            db_obj.deleted_at = datetime.utcnow()
            self.db.commit()
            return True
        return False
