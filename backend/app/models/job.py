"""Job and Application Models"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric, JSON, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.database import Base

class JobPost(Base):
    """Job Post Model"""
    __tablename__ = "job_post"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey('company.id'), nullable=False)
    
    title = Column(String(255), nullable=False)
    description = Column(String(2000))
    responsibilities = Column(JSON, default=[])
    requirements = Column(JSON, default=[])
    
    job_type = Column(String(50))  # full-time, part-time, contract, internship
    experience_required = Column(Integer)  # in years
    
    salary_min = Column(Numeric(12, 2))
    salary_max = Column(Numeric(12, 2))
    currency = Column(String(10), default="USD")
    
    location = Column(String(255))
    is_remote = Column(Boolean, default=False)
    
    required_skills = Column(JSON, default=[])
    preferred_skills = Column(JSON, default=[])
    
    posted_date = Column(DateTime, default=datetime.utcnow)
    deadline = Column(DateTime)
    
    is_active = Column(Boolean, default=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

    # Relationships
    company = relationship("Company", back_populates="job_posts")
    applications = relationship("JobApplication", back_populates="job_post")

    def __repr__(self):
        return f"<JobPost {self.title}>"

class JobApplication(Base):
    """Job Application Model"""
    __tablename__ = "job_application"

    id = Column(Integer, primary_key=True, index=True)
    job_post_id = Column(Integer, ForeignKey('job_post.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    resume_id = Column(Integer, ForeignKey('resume.id'))
    
    status = Column(String(50), default="applied")  # applied, reviewed, shortlisted, rejected, interview, offered, accepted, declined
    
    cover_letter = Column(String(2000))
    application_date = Column(DateTime, default=datetime.utcnow)
    
    interview_round = Column(Integer, default=0)
    interview_date = Column(DateTime, nullable=True)
    interview_feedback = Column(String(1000))
    
    offered_salary = Column(Numeric(12, 2))
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

    # Relationships
    job_post = relationship("JobPost", back_populates="applications")

    def __repr__(self):
        return f"<JobApplication {self.id}>"
