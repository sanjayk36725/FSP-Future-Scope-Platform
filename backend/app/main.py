"""
FSP (Future Scope Platform) - Main Application Entry Point
Enterprise AI-Powered Unified Platform
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import logging
from datetime import datetime
import os

from app.config import settings
from app.middleware.error_handler import setup_exception_handlers
from app.api.v1 import (
    auth,
    users,
    dashboard,
    students,
    faculty,
    developers,
    recruiters,
    hr_employees,
    administrators,
    ai_helper,
    files
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="FSP (Future Scope Platform)",
    description="Enterprise AI-Powered Unified Platform",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup exception handlers
setup_exception_handlers(app)

# Mount static files
if os.path.exists("uploads"):
    app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# API Routes
api_prefix = "/api/v1"

# Authentication Routes
app.include_router(auth.router, prefix=f"{api_prefix}/auth", tags=["Authentication"])

# User Management Routes
app.include_router(users.router, prefix=f"{api_prefix}/users", tags=["Users"])

# Dashboard Routes
app.include_router(dashboard.router, prefix=f"{api_prefix}/dashboard", tags=["Dashboard"])

# Domain-Specific Routes
app.include_router(students.router, prefix=f"{api_prefix}/students", tags=["Students"])
app.include_router(faculty.router, prefix=f"{api_prefix}/faculty", tags=["Faculty"])
app.include_router(developers.router, prefix=f"{api_prefix}/developers", tags=["Developers"])
app.include_router(recruiters.router, prefix=f"{api_prefix}/recruiters", tags=["Recruiters"])
app.include_router(hr_employees.router, prefix=f"{api_prefix}/hr", tags=["HR"])
app.include_router(administrators.router, prefix=f"{api_prefix}/administrators", tags=["Administrators"])

# AI Helper Routes
app.include_router(ai_helper.router, prefix=f"{api_prefix}/ai", tags=["AI Helper & Agents"])

# File Management Routes
app.include_router(files.router, prefix=f"{api_prefix}/files", tags=["File Management"])

# Health Check Endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "FSP-Platform",
        "version": "1.0.0"
    }

# Root Endpoint
@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "name": "FSP (Future Scope Platform)",
        "version": "1.0.0",
        "description": "Enterprise AI-Powered Unified Platform",
        "documentation": "/api/docs",
        "status": "running",
        "timestamp": datetime.utcnow().isoformat()
    }

# Startup Event
@app.on_event("startup")
async def startup_event():
    """Run on application startup"""
    logger.info("🚀 FSP Platform Starting Up")
    logger.info(f"Environment: {settings.ENVIRONMENT}")
    logger.info(f"Database: {settings.DATABASE_URL}")
    logger.info(f"Debug Mode: {settings.DEBUG}")

# Shutdown Event
@app.on_event("shutdown")
async def shutdown_event():
    """Run on application shutdown"""
    logger.info("🛑 FSP Platform Shutting Down")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level="info"
    )
