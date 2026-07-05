# FSP (Future Scope Platform) Backend

Enterprise AI-Powered Unified Platform Backend API

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- PostgreSQL 14+ (or SQLite for development)
- Redis (optional, for caching)
- Virtual Environment

### Setup

1. **Clone Repository**
```bash
git clone https://github.com/sanjayk36725/FSP-Future-Scope-Platform.git
cd FSP-Future-Scope-Platform/backend
```

2. **Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure Environment**
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. **Initialize Database**
```bash
python init_db.py
```

6. **Run Development Server**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API will be available at `http://localhost:8000`

## 📚 API Documentation

- **Swagger UI**: http://localhost:8000/api/docs
- **ReDoc**: http://localhost:8000/api/redoc
- **OpenAPI JSON**: http://localhost:8000/api/openapi.json

## 🐳 Docker Deployment

### Start with Docker Compose
```bash
cd ..
docker-compose up -d
```

### Services
- Backend API: http://localhost:8000
- PostgreSQL: localhost:5432
- Redis: localhost:6379

## 📁 Project Structure

```
backend/
├── app/
│   ├── api/v1/           # API endpoints
│   ├── models/           # Database models
│   ├── schemas/          # Pydantic schemas
│   ├── services/         # Business logic
│   ├── repositories/     # Data access layer
│   ├── utils/            # Utility functions
│   ├── middleware/       # Middleware
│   ├── db/               # Database config
│   ├── ai_agents/        # AI agents
│   ├── config.py         # Configuration
│   ├── dependencies.py   # Dependency injection
│   └── main.py           # Application entry
├── tests/                # Unit tests
├── requirements.txt      # Dependencies
├── Dockerfile            # Container image
└── init_db.py           # Database initialization
```

## 🔐 Authentication

### Login
```bash
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "password123"
  }'
```

### Use Access Token
```bash
curl -H "Authorization: Bearer <access_token>" \
  http://localhost:8000/api/v1/users/profile
```

## 🤖 AI Agents

Available AI agents:
- Personal Tutor
- Coding Mentor
- Resume Review
- Mock Interview
- Code Review
- And 30+ more...

## 📊 Database

### Tables
- users
- roles
- permissions
- students
- faculty
- companies
- job_posts
- job_applications
- resumes
- ai_conversations
- ai_messages
- files
- notifications
- audit_logs
- activity_logs

## 🧪 Testing

```bash
pytest tests/
```

## 📝 Environment Variables

See `.env.example` for all available configuration options.

## 🚀 Deployment

### Render.com
1. Push to GitHub
2. Connect Render to GitHub
3. Set environment variables
4. Deploy

### AWS/GCP/Azure
Use Docker image with your preferred cloud platform.

## 📖 API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register user
- `POST /api/v1/auth/login` - Login user
- `POST /api/v1/auth/refresh` - Refresh token
- `POST /api/v1/auth/forgot-password` - Request password reset
- `POST /api/v1/auth/reset-password` - Reset password

### Users
- `GET /api/v1/users/profile` - Get user profile
- `PUT /api/v1/users/profile` - Update profile
- `GET /api/v1/users/` - List users (admin)
- `GET /api/v1/users/{user_id}` - Get user details

### Dashboard
- `GET /api/v1/dashboard/overview` - Dashboard overview
- `GET /api/v1/dashboard/statistics` - Statistics
- `GET /api/v1/dashboard/recent-activities` - Recent activities

### AI
- `GET /api/v1/ai/agents` - List AI agents
- `POST /api/v1/ai/chat` - Send chat message
- `GET /api/v1/ai/conversations` - Get conversations
- `POST /api/v1/ai/upload-for-analysis` - Upload file for analysis

## 🔗 Related

- [Frontend Repository](../frontend)
- [Database Schema](../docs/DATABASE_SCHEMA.md)
- [API Documentation](../docs/API_DOCUMENTATION.md)

## 📄 License

MIT License - See LICENSE file

## 👥 Support

For issues and questions, create a GitHub issue.
