"""Security Utilities"""

import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from typing import Optional, Dict, Any

from app.config import settings

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Hash password using bcrypt"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password against hash"""
    return pwd_context.verify(plain_password, hashed_password)

def create_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    """Create JWT token"""
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    
    return encoded_jwt

def create_access_token(user_id: int) -> str:
    """Create access token"""
    data = {"sub": str(user_id), "type": "access"}
    return create_token(data)

def create_refresh_token(user_id: int) -> str:
    """Create refresh token"""
    data = {"sub": str(user_id), "type": "refresh"}
    expires_delta = timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    return create_token(data, expires_delta)

def verify_token(token: str) -> Dict[str, Any]:
    """Verify and decode JWT token"""
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        return payload
    except jwt.InvalidTokenError as e:
        raise jwt.InvalidTokenError(f"Invalid token: {str(e)}")

def generate_email_verification_token(email: str) -> str:
    """Generate email verification token"""
    data = {"sub": email, "type": "email_verification"}
    expires_delta = timedelta(hours=24)
    return create_token(data, expires_delta)

def generate_password_reset_token(email: str) -> str:
    """Generate password reset token"""
    data = {"sub": email, "type": "password_reset"}
    expires_delta = timedelta(hours=1)
    return create_token(data, expires_delta)
