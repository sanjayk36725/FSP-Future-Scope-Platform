"""User Service"""

from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
import logging

from app.models.user import User
from app.schemas.user import UserUpdate
from app.utils import paginate

logger = logging.getLogger(__name__)

class UserService:
    """User Service"""

    async def update_user(self, user_id: int, user_data: UserUpdate, db: Session) -> User:
        """Update user profile"""
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise ValueError("User not found")

        # Update fields
        if user_data.first_name:
            user.first_name = user_data.first_name
        if user_data.last_name:
            user.last_name = user_data.last_name
        if user_data.phone:
            user.phone = user_data.phone
        if user_data.bio:
            user.bio = user_data.bio
        if user_data.profile_picture:
            user.profile_picture = user_data.profile_picture

        user.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(user)

        logger.info(f"User updated: {user.email}")
        return user

    async def get_user_by_id(self, user_id: int, db: Session) -> Optional[User]:
        """Get user by ID"""
        return db.query(User).filter(User.id == user_id).first()

    async def get_user_by_email(self, email: str, db: Session) -> Optional[User]:
        """Get user by email"""
        return db.query(User).filter(User.email == email).first()

    async def list_users(self, page: int, page_size: int, db: Session) -> List[User]:
        """List all users with pagination"""
        query = db.query(User).filter(User.deleted_at.is_(None))
        return paginate(query, page, page_size).all()

    async def delete_user(self, user_id: int, db: Session):
        """Soft delete user"""
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise ValueError("User not found")

        user.deleted_at = datetime.utcnow()
        user.is_active = False
        db.commit()

        logger.info(f"User deleted: {user.email}")
