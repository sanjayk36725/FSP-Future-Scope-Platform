#!/usr/bin/env python
"""Production-ready main application file"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
from datetime import datetime

from app.config import settings
from app.middleware.error_handler import setup_exception_handlers
from app.api.v1 import (
    auth, users, dashboard, students, faculty, developers,
    recruiters, hr_employees, administrators, ai_helper, files
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI
app = FastAPI(
    title="FSP (Future Scope Platform)",
    description="Enterprise AI-Powered Unified Platform",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup exception handlers
setup_exception_handlers(app)

# API prefix
api_prefix = "/api/v1"

# Include routers
app.include_router(auth.router, prefix=f"{api_prefix}/auth", tags=["Authentication"])
app.include_router(users.router, prefix=f"{api_prefix}/users", tags=["Users"])
app.include_router(dashboard.router, prefix=f"{api_prefix}/dashboard", tags=["Dashboard"])
app.include_router(students.router, prefix=f"{api_prefix}/students", tags=["Students"])
app.include_router(faculty.router, prefix=f"{api_prefix}/faculty", tags=["Faculty"])
app.include_router(developers.router, prefix=f"{api_prefix}/developers", tags=["Developers"])
app.include_router(recruiters.router, prefix=f"{api_prefix}/recruiters", tags=["Recruiters"])
app.include_router(hr_employees.router, prefix=f"{api_prefix}/hr", tags=["HR"])
app.include_router(administrators.router, prefix=f"{api_prefix}/administrators", tags=["Administrators"])
app.include_router(ai_helper.router, prefix=f"{api_prefix}/ai", tags=["AI Helper & Agents"])
app.include_router(files.router, prefix=f"{api_prefix}/files", tags=["File Management"])

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "FSP-Platform",
        "version": "1.0.0"
    }

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "name": "FSP (Future Scope Platform)",
        "version": "1.0.0",
        "status": "running",
        "docs": "/api/docs",
        "timestamp": datetime.utcnow().isoformat()
    }

@app.on_event("startup")
async def startup_event():
    """Startup event"""
    logger.info("🚀 FSP Platform Starting")
    logger.info(f"Environment: {settings.ENVIRONMENT}")

@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event"""
    logger.info("🛑 FSP Platform Shutting Down")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
