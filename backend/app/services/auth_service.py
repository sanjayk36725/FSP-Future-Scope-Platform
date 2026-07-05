"""Authentication Service"""

from sqlalchemy.orm import Session
from datetime import datetime
import logging

from app.models.user import User, Role
from app.schemas.user import UserCreate, UserLogin, ChangePassword, TokenSchema
from app.utils.security import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
    verify_token
)
from app.utils.validators import validate_password_strength, validate_email

logger = logging.getLogger(__name__)

class AuthService:
    """Authentication Service"""

    async def register_user(self, user_data: UserCreate, db: Session) -> User:
        """Register new user"""
        # Validate email
        if not validate_email(user_data.email):
            raise ValueError("Invalid email format")

        # Check if user exists
        existing_user = db.query(User).filter(
            (User.email == user_data.email) | (User.username == user_data.username)
        ).first()
        if existing_user:
            raise ValueError("User with this email or username already exists")

        # Validate password strength
        is_valid, error_msg = validate_password_strength(user_data.password)
        if not is_valid:
            raise ValueError(error_msg)

        # Get role
        role = db.query(Role).filter(Role.name == user_data.role).first()
        if not role:
            raise ValueError(f"Role '{user_data.role}' does not exist")

        # Create user
        user = User(
            email=user_data.email,
            username=user_data.username,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            phone=user_data.phone,
            password_hash=hash_password(user_data.password),
        )
        user.roles.append(role)

        db.add(user)
        db.commit()
        db.refresh(user)

        logger.info(f"User registered: {user.email}")
        return user

    async def login_user(self, credentials: UserLogin, db: Session) -> TokenSchema:
        """Login user and return tokens"""
        # Find user
        user = db.query(User).filter(User.email == credentials.email).first()
        if not user or not verify_password(credentials.password, user.password_hash):
            raise ValueError("Invalid email or password")

        if not user.is_active:
            raise ValueError("User account is inactive")

        # Update last login
        user.last_login = datetime.utcnow()
        db.commit()

        # Create tokens
        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        logger.info(f"User logged in: {user.email}")

        return TokenSchema(
            access_token=access_token,
            refresh_token=refresh_token,
            expires_in=30 * 60  # 30 minutes in seconds
        )

    async def refresh_token(self, refresh_token: str) -> TokenSchema:
        """Refresh access token"""
        try:
            payload = verify_token(refresh_token)
            if payload.get("type") != "refresh":
                raise ValueError("Invalid token type")
            user_id = int(payload.get("sub"))
        except Exception as e:
            raise ValueError(f"Invalid refresh token: {str(e)}")

        access_token = create_access_token(user_id)
        new_refresh_token = create_refresh_token(user_id)

        return TokenSchema(
            access_token=access_token,
            refresh_token=new_refresh_token,
            expires_in=30 * 60
        )

    async def send_password_reset_email(self, email: str, db: Session):
        """Send password reset email"""
        user = db.query(User).filter(User.email == email).first()
        if not user:
            # Don't reveal if email exists
            return

        # TODO: Send email with reset link
        logger.info(f"Password reset email sent to: {email}")

    async def reset_password(self, token: str, new_password: str, db: Session):
        """Reset password with token"""
        try:
            payload = verify_token(token)
            if payload.get("type") != "password_reset":
                raise ValueError("Invalid token type")
            email = payload.get("sub")
        except Exception as e:
            raise ValueError(f"Invalid reset token: {str(e)}")

        is_valid, error_msg = validate_password_strength(new_password)
        if not is_valid:
            raise ValueError(error_msg)

        user = db.query(User).filter(User.email == email).first()
        if not user:
            raise ValueError("User not found")

        user.password_hash = hash_password(new_password)
        db.commit()

        logger.info(f"Password reset for user: {email}")

    async def change_password(self, user: User, data: ChangePassword, db: Session):
        """Change user password"""
        if not verify_password(data.current_password, user.password_hash):
            raise ValueError("Current password is incorrect")

        is_valid, error_msg = validate_password_strength(data.new_password)
        if not is_valid:
            raise ValueError(error_msg)

        user.password_hash = hash_password(data.new_password)
        db.commit()

        logger.info(f"Password changed for user: {user.email}")

    async def verify_email(self, token: str, db: Session):
        """Verify user email"""
        try:
            payload = verify_token(token)
            if payload.get("type") != "email_verification":
                raise ValueError("Invalid token type")
            email = payload.get("sub")
        except Exception as e:
            raise ValueError(f"Invalid verification token: {str(e)}")

        user = db.query(User).filter(User.email == email).first()
        if not user:
            raise ValueError("User not found")

        user.is_email_verified = True
        user.email_verified_at = datetime.utcnow()
        db.commit()

        logger.info(f"Email verified for user: {email}")
