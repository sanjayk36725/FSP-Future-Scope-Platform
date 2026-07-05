"""Validators"""

import re
from typing import Optional

def validate_email(email: str) -> bool:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone: str) -> bool:
    """Validate phone number"""
    pattern = r'^\+?1?\d{9,15}$'
    return re.match(pattern, phone) is not None

def validate_password_strength(password: str) -> tuple[bool, Optional[str]]:
    """Validate password strength"""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter"
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter"
    if not re.search(r'[0-9]', password):
        return False, "Password must contain at least one digit"
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character"
    return True, None

def validate_file_extension(filename: str, allowed_extensions: list) -> bool:
    """Validate file extension"""
    if '.' not in filename:
        return False
    ext = filename.rsplit('.', 1)[1].lower()
    return ext in allowed_extensions

def validate_file_size(file_size: int, max_size: int) -> bool:
    """Validate file size"""
    return file_size <= max_size
