"""User and Authentication Models"""

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Table, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from app.db.database import Base

# Association tables
user_role_association = Table(
    'user_role_association',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('role_id', Integer, ForeignKey('role.id'), primary_key=True)
)

role_permission_association = Table(
    'role_permission_association',
    Base.metadata,
    Column('role_id', Integer, ForeignKey('role.id'), primary_key=True),
    Column('permission_id', Integer, ForeignKey('permission.id'), primary_key=True)
)

class RoleEnum(str, enum.Enum):
    """User Role Enumeration"""
    STUDENT = "student"
    FACULTY = "faculty"
    DEVELOPER = "developer"
    RECRUITER = "recruiter"
    HR_MANAGER = "hr_manager"
    ADMINISTRATOR = "administrator"

class Role(Base):
    """User Role Model"""
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True, nullable=False)
    description = Column(String(255))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    permissions = relationship(
        "Permission",
        secondary=role_permission_association,
        back_populates="roles"
    )
    users = relationship("User", secondary=user_role_association, back_populates="roles")

    def __repr__(self):
        return f"<Role {self.name}>"

class Permission(Base):
    """Permission Model"""
    __tablename__ = "permission"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True, nullable=False)
    description = Column(String(255))
    code = Column(String(50), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    roles = relationship(
        "Role",
        secondary=role_permission_association,
        back_populates="permissions"
    )

    def __repr__(self):
        return f"<Permission {self.name}>"

class User(Base):
    """Core User Model"""
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(100), unique=True, index=True, nullable=False)
    first_name = Column(String(100))
    last_name = Column(String(100))
    phone = Column(String(20))
    password_hash = Column(String(255), nullable=False)
    profile_picture = Column(String(500))
    bio = Column(String(500))
    
    is_active = Column(Boolean, default=True)
    is_email_verified = Column(Boolean, default=False)
    email_verified_at = Column(DateTime, nullable=True)
    
    last_login = Column(DateTime, nullable=True)
    last_login_ip = Column(String(50))
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)  # Soft delete

    # Relationships
    roles = relationship(
        "Role",
        secondary=user_role_association,
        back_populates="users"
    )
    student = relationship("Student", back_populates="user", uselist=False)
    faculty = relationship("Faculty", back_populates="user", uselist=False)
    developer = relationship("Developer", back_populates="user", uselist=False)
    recruiter = relationship("Recruiter", back_populates="user", uselist=False)
    hr_employee = relationship("HREmployee", back_populates="user", uselist=False)
    administrator = relationship("Administrator", back_populates="user", uselist=False)
    
    ai_conversations = relationship("AIConversation", back_populates="user")
    notifications = relationship("Notification", back_populates="user")
    uploaded_files = relationship("FileUpload", back_populates="user")

    def __repr__(self):
        return f"<User {self.username}>"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
