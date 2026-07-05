"""User Repository"""

from sqlalchemy.orm import Session
from typing import Optional

from app.models.user import User
from app.repositories.base_repository import BaseRepository

class UserRepository(BaseRepository[User]):
    """User repository for database operations"""

    def get_by_email(self, email: str) -> Optional[User]:
        """Get user by email"""
        return self.db.query(User).filter(User.email == email).first()

    def get_by_username(self, username: str) -> Optional[User]:
        """Get user by username"""
        return self.db.query(User).filter(User.username == username).first()

    def get_active_users(self, skip: int = 0, limit: int = 100):
        """Get active users"""
        return self.db.query(User).filter(
            User.is_active == True,
            User.deleted_at.is_(None)
        ).offset(skip).limit(limit).all()
