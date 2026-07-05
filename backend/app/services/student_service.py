"""Student Service"""

from sqlalchemy.orm import Session
from datetime import datetime
import logging

from app.models.student import Student
from app.schemas.student import StudentUpdate

logger = logging.getLogger(__name__)

class StudentService:
    """Student Service"""

    async def get_student_profile(self, user_id: int, db: Session) -> Student:
        """Get student profile"""
        student = db.query(Student).filter(Student.user_id == user_id).first()
        if not student:
            raise ValueError("Student profile not found")
        return student

    async def update_student_profile(self, user_id: int, student_data: StudentUpdate, db: Session) -> Student:
        """Update student profile"""
        student = db.query(Student).filter(Student.user_id == user_id).first()
        if not student:
            raise ValueError("Student profile not found")

        if student_data.semester is not None:
            student.semester = student_data.semester
        if student_data.cgpa is not None:
            student.cgpa = student_data.cgpa
        if student_data.is_placed is not None:
            student.is_placed = student_data.is_placed
        if student_data.placed_company is not None:
            student.placed_company = student_data.placed_company
        if student_data.placed_package is not None:
            student.placed_package = student_data.placed_package

        student.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(student)

        logger.info(f"Student profile updated: {user_id}")
        return student
