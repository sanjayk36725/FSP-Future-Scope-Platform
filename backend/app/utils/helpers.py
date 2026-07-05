"""Helper Functions"""

from typing import List, Dict, Any, Optional
from datetime import datetime
import os
import uuid

def paginate(query, page: int, page_size: int):
    """Paginate query results"""
    skip = (page - 1) * page_size
    return query.offset(skip).limit(page_size)

def generate_unique_filename(original_filename: str) -> str:
    """Generate unique filename"""
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    unique_id = str(uuid.uuid4())[:8]
    name, ext = os.path.splitext(original_filename)
    return f"{name}_{timestamp}_{unique_id}{ext}"

def format_response(status: str, message: str, data: Optional[Any] = None) -> Dict[str, Any]:
    """Format API response"""
    return {
        "status": status,
        "message": message,
        "data": data,
        "timestamp": datetime.utcnow().isoformat()
    }

def format_error_response(error_code: str, message: str, detail: Optional[str] = None) -> Dict[str, Any]:
    """Format error response"""
    return {
        "status": "error",
        "error_code": error_code,
        "message": message,
        "detail": detail,
        "timestamp": datetime.utcnow().isoformat()
    }

def extract_user_agent(user_agent_string: str) -> Dict[str, str]:
    """Extract user agent information"""
    # Simple extraction logic
    if "Mobile" in user_agent_string:
        device = "mobile"
    elif "Tablet" in user_agent_string:
        device = "tablet"
    else:
        device = "desktop"
    
    return {"device_type": device}
