#!/usr/bin/env python
"""Database initialization and seeding"""

from app.db.database import init_db, Base, engine
from app.models.user import Role, Permission
from sqlalchemy.orm import sessionmaker
import logging

logger = logging.getLogger(__name__)

def init_roles(db):
    """Initialize default roles"""
    roles_data = [
        {"name": "student", "description": "Student role"},
        {"name": "faculty", "description": "Faculty role"},
        {"name": "developer", "description": "Developer role"},
        {"name": "recruiter", "description": "Recruiter role"},
        {"name": "hr_manager", "description": "HR Manager role"},
        {"name": "administrator", "description": "Administrator role"},
    ]
    
    for role_data in roles_data:
        existing = db.query(Role).filter(Role.name == role_data["name"]).first()
        if not existing:
            role = Role(**role_data)
            db.add(role)
    
    db.commit()
    logger.info("Roles initialized")

def init_permissions(db):
    """Initialize default permissions"""
    permissions_data = [
        {"name": "View Dashboard", "code": "view_dashboard"},
        {"name": "View Profile", "code": "view_profile"},
        {"name": "Edit Profile", "code": "edit_profile"},
        {"name": "Manage Users", "code": "manage_users"},
        {"name": "Manage Roles", "code": "manage_roles"},
        {"name": "Manage System", "code": "manage_system"},
    ]
    
    for perm_data in permissions_data:
        existing = db.query(Permission).filter(Permission.code == perm_data["code"]).first()
        if not existing:
            permission = Permission(**perm_data)
            db.add(permission)
    
    db.commit()
    logger.info("Permissions initialized")

def main():
    """Initialize database"""
    # Create tables
    init_db()
    
    # Create session
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    
    try:
        # Initialize data
        init_roles(db)
        init_permissions(db)
        logger.info("Database initialization completed successfully")
    finally:
        db.close()

if __name__ == "__main__":
    main()
