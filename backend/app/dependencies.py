"""Dependency Injection for FastAPI"""

from fastapi import Depends, HTTPException, status, Header
from sqlalchemy.orm import Session
from typing import Optional
import jwt
from datetime import datetime, timedelta

from app.config import settings
from app.db.session import SessionLocal
from app.models.user import User
from app.utils.security import verify_token

def get_db() -> Session:
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_current_user(
    token: str = Depends(lambda: None),
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db)
) -> User:
    """Get current authenticated user"""
    token = token or (authorization.split()[1] if authorization else None)
    
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    try:
        payload = verify_token(token)
        user_id: int = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    
    return user

async def get_current_student(current_user: User = Depends(get_current_user)) -> User:
    """Get current student user"""
    if current_user.role.name != "student":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied. Student role required."
        )
    return current_user

async def get_current_faculty(current_user: User = Depends(get_current_user)) -> User:
    """Get current faculty user"""
    if current_user.role.name != "faculty":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied. Faculty role required."
        )
    return current_user

async def get_current_recruiter(current_user: User = Depends(get_current_user)) -> User:
    """Get current recruiter user"""
    if current_user.role.name != "recruiter":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied. Recruiter role required."
        )
    return current_user

async def get_current_hr_manager(current_user: User = Depends(get_current_user)) -> User:
    """Get current HR manager user"""
    if current_user.role.name != "hr_manager":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied. HR Manager role required."
        )
    return current_user

async def get_current_admin(current_user: User = Depends(get_current_user)) -> User:
    """Get current admin user"""
    if current_user.role.name != "administrator":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied. Administrator role required."
        )
    return current_user
