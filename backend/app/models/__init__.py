"""Database Models Package"""

from app.models.user import User, Role, Permission
from app.models.student import Student
from app.models.faculty import Faculty
from app.models.developer import Developer
from app.models.recruiter import Recruiter
from app.models.hr_employee import HREmployee
from app.models.administrator import Administrator
from app.models.course import Course
from app.models.job import JobPost, JobApplication
from app.models.company import Company
from app.models.resume import Resume
from app.models.ai_conversation import AIConversation, AIMessage
from app.models.file import FileUpload
from app.models.notification import Notification
from app.models.audit_log import AuditLog, ActivityLog

__all__ = [
    "User",
    "Role",
    "Permission",
    "Student",
    "Faculty",
    "Developer",
    "Recruiter",
    "HREmployee",
    "Administrator",
    "Course",
    "JobPost",
    "JobApplication",
    "Company",
    "Resume",
    "AIConversation",
    "AIMessage",
    "FileUpload",
    "Notification",
    "AuditLog",
    "ActivityLog",
]
