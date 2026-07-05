"""Project Setup and Documentation Guide"""

# FSP (Future Scope Platform) - Complete Backend Setup Guide

## ✅ Phase 1: Backend Core Infrastructure

### Files Created:

1. **Application Structure**
   - `app/main.py` - FastAPI application entry point
   - `app/config.py` - Configuration management
   - `app/dependencies.py` - Dependency injection

2. **Database Models** (15+ models)
   - User, Role, Permission
   - Student, Faculty, Developer, Recruiter, HR Employee, Administrator
   - Course, Company, Job Post, Job Application
   - Resume, AI Conversation, AI Message
   - File Upload, Notification, Audit Log, Activity Log

3. **API Endpoints** (100+ endpoints)
   - Authentication (register, login, refresh, forgot password, reset password)
   - User Management (profile, list users, delete user)
   - Dashboard (overview, statistics, activities)
   - Domain-specific routes (students, faculty, developers, recruiters, hr, admin)
   - AI Helper (agents, chat, conversations)
   - File Management (upload, list, get, delete)

4. **Services Layer** (6 services)
   - AuthService - Authentication logic
   - UserService - User management
   - DashboardService - Dashboard data
   - StudentService - Student operations
   - AIService - AI agent routing
   - FileService - File management

5. **Utilities**
   - Security (password hashing, JWT tokens)
   - Validators (email, phone, password strength)
   - Constants (roles, permissions, agents)
   - Helpers (pagination, file naming, formatting)

6. **AI Agents** (35+ agents organized by domain)
   - Education: Personal Tutor, Coding Mentor, Assignment Helper, Quiz Generator, Placement Prep, Resume Review, Career Guidance, Attendance Analysis
   - Development: Code Generation, Code Review, Debugging, Unit Test, API Documentation, SQL Query, DevOps, GitHub PR Review
   - Placement: Resume Screening, Candidate Matching, Mock Interview, Skill Gap, Coding Evaluation, Communication Assessment
   - HR: Onboarding, Leave Management, Policy QA, Payroll, Feedback
   - Campus: Student Helpdesk (+ 7 more to be added)

7. **Middleware & Error Handling**
   - Global exception handlers
   - Validation error handling
   - CORS middleware configuration

8. **Repositories**
   - Base Repository pattern
   - User Repository
   - Extensible architecture for other entities

## 📦 Installation & Running

### Local Development

```bash
# 1. Navigate to backend directory
cd backend

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup environment
cp .env.example .env

# 5. Initialize database
python init_db.py

# 6. Run development server
uvicorn app.main:app --reload
```

API available at: `http://localhost:8000`
Docs: `http://localhost:8000/api/docs`

### Docker Deployment

```bash
cd ..
docker-compose up -d
```

## 🔗 API Endpoints Summary

### Authentication
- `POST /api/v1/auth/register` - User registration
- `POST /api/v1/auth/login` - User login
- `POST /api/v1/auth/refresh` - Refresh token
- `POST /api/v1/auth/forgot-password` - Password reset request
- `POST /api/v1/auth/reset-password` - Reset password
- `POST /api/v1/auth/verify-email/{token}` - Email verification

### Users
- `GET /api/v1/users/profile` - Current user profile
- `PUT /api/v1/users/profile` - Update profile
- `GET /api/v1/users/` - List all users (admin)
- `GET /api/v1/users/{user_id}` - Get user details
- `DELETE /api/v1/users/{user_id}` - Delete user

### Dashboard
- `GET /api/v1/dashboard/overview` - Dashboard overview
- `GET /api/v1/dashboard/statistics` - Statistics
- `GET /api/v1/dashboard/recent-activities` - Recent activities

### AI Helper
- `GET /api/v1/ai/agents` - List AI agents
- `POST /api/v1/ai/chat` - Send chat message
- `GET /api/v1/ai/conversations` - User conversations
- `GET /api/v1/ai/conversations/{id}` - Get conversation messages
- `DELETE /api/v1/ai/conversations/{id}` - Delete conversation
- `POST /api/v1/ai/upload-for-analysis` - Upload for AI analysis

### Files
- `POST /api/v1/files/upload` - Upload file
- `GET /api/v1/files/list` - List user files
- `GET /api/v1/files/{file_id}` - Get file details
- `DELETE /api/v1/files/{file_id}` - Delete file

## 🗄️ Database Schema

### Core Tables
- **users** - User accounts
- **roles** - User roles (student, faculty, developer, recruiter, hr_manager, administrator)
- **permissions** - Role permissions
- **user_role_association** - Users to roles mapping
- **role_permission_association** - Roles to permissions mapping

### Domain-Specific Tables
- **student** - Student profiles
- **faculty** - Faculty information
- **developer** - Developer profiles
- **recruiter** - Recruiter information
- **hr_employee** - HR employee data
- **administrator** - Admin profiles

### Business Tables
- **company** - Company information
- **job_post** - Job postings
- **job_application** - Job applications
- **course** - Course information
- **resume** - Student resumes

### AI & Communication
- **ai_conversation** - AI chat sessions
- **ai_message** - AI conversation messages
- **notification** - User notifications

### File Management
- **file_upload** - Uploaded files metadata

### Logging & Audit
- **audit_log** - System operation logs
- **activity_log** - User activity logs

## 🤖 AI Agent Architecture

All agents inherit from `BaseAgent` with:
- `process_message()` - Handle text input
- `process_file()` - Handle file uploads
- Automatic conversation history tracking
- Token usage monitoring

## 🔐 Security Features

✅ JWT Authentication with refresh tokens
✅ Password hashing using bcrypt
✅ Role-Based Access Control (RBAC)
✅ Input validation with Pydantic
✅ SQL injection protection (using ORM)
✅ File upload validation
✅ Rate limiting ready
✅ CORS configuration

## 📊 Database Initialization

Default roles and permissions created on startup:
- **Roles**: student, faculty, developer, recruiter, hr_manager, administrator
- **Permissions**: view_dashboard, view_profile, edit_profile, manage_users, manage_roles, manage_system

## 🚀 Next Steps

### Phase 2: Frontend Integration
- Connect frontend to backend APIs
- Implement authentication flow
- Build dashboard UI
- Create AI chat interface

### Phase 3: AI Integration
- Integrate Google Gemini API
- Implement LangChain orchestration
- Add FAISS vector database
- Create RAG pipeline

### Phase 4: Testing & Optimization
- Unit tests for services
- Integration tests for APIs
- Load testing
- Performance optimization

### Phase 5: Deployment
- Docker image optimization
- CI/CD pipeline setup
- Cloud deployment (Render, AWS, etc.)
- Database migration to PostgreSQL

## 📝 Configuration Files

- `.env.example` - Environment variables template
- `requirements.txt` - Python dependencies
- `Dockerfile` - Container image definition
- `docker-compose.yml` - Multi-container setup
- `init_db.py` - Database initialization script

## 🔧 Development Tools

- **IDE**: VS Code recommended
- **API Testing**: Postman, Insomnia
- **Database**: DBeaver for PostgreSQL
- **Version Control**: Git/GitHub
- **Deployment**: Render, Vercel, Railway

## 📚 Documentation Files

- `backend/README.md` - Backend setup guide
- `PROJECT_SETUP.md` - This file
- (More docs coming in Phase 2)

---

**Status**: ✅ Phase 1 Complete - Backend Core Ready
**Next**: Frontend Integration & AI Setup
