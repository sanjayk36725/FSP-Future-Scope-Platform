"""Dashboard Service"""

from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
import logging

from app.models.user import User
from app.models.student import Student
from app.models.job import JobPost, JobApplication
from app.models.activity_log import ActivityLog

logger = logging.getLogger(__name__)

class DashboardService:
    """Dashboard Service"""

    async def get_dashboard_overview(self, user: User, db: Session) -> dict:
        """Get dashboard overview based on user role"""
        role = user.roles[0].name if user.roles else None

        if role == "student":
            return await self._get_student_dashboard(user, db)
        elif role == "faculty":
            return await self._get_faculty_dashboard(user, db)
        elif role == "recruiter":
            return await self._get_recruiter_dashboard(user, db)
        elif role == "hr_manager":
            return await self._get_hr_dashboard(user, db)
        elif role == "administrator":
            return await self._get_admin_dashboard(user, db)
        else:
            return {"message": "Dashboard not available for this role"}

    async def _get_student_dashboard(self, user: User, db: Session) -> dict:
        """Get student dashboard"""
        student = db.query(Student).filter(Student.user_id == user.id).first()
        
        return {
            "role": "student",
            "student_info": {
                "name": user.full_name,
                "roll_number": student.roll_number if student else None,
                "cgpa": float(student.cgpa) if student else 0.0,
                "semester": student.semester if student else None,
            },
            "quick_stats": {
                "placement_status": student.is_placed if student else "not_placed",
                "applications": 0,
                "interviews": 0,
                "courses": 0,
            }
        }

    async def _get_faculty_dashboard(self, user: User, db: Session) -> dict:
        """Get faculty dashboard"""
        return {
            "role": "faculty",
            "quick_stats": {
                "courses": 0,
                "students": 0,
                "assignments": 0,
                "pending_reviews": 0,
            }
        }

    async def _get_recruiter_dashboard(self, user: User, db: Session) -> dict:
        """Get recruiter dashboard"""
        return {
            "role": "recruiter",
            "quick_stats": {
                "open_positions": 0,
                "applications": 0,
                "interviews": 0,
                "offers": 0,
            }
        }

    async def _get_hr_dashboard(self, user: User, db: Session) -> dict:
        """Get HR dashboard"""
        return {
            "role": "hr_manager",
            "quick_stats": {
                "employees": 0,
                "leave_requests": 0,
                "pending_approvals": 0,
                "payroll_status": "pending",
            }
        }

    async def _get_admin_dashboard(self, user: User, db: Session) -> dict:
        """Get admin dashboard"""
        return {
            "role": "administrator",
            "quick_stats": {
                "total_users": db.query(func.count(User.id)).scalar(),
                "active_users": db.query(func.count(User.id)).filter(User.is_active == True).scalar(),
                "total_students": db.query(func.count(Student.id)).scalar(),
            }
        }

    async def get_statistics(self, user: User, db: Session) -> dict:
        """Get dashboard statistics"""
        return {
            "timestamp": datetime.utcnow().isoformat(),
            "statistics": {}
        }

    async def get_recent_activities(self, user_id: int, limit: int, db: Session) -> list:
        """Get recent user activities"""
        activities = db.query(ActivityLog).filter(
            ActivityLog.user_id == user_id
        ).order_by(ActivityLog.created_at.desc()).limit(limit).all()
        return activities
