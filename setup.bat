@echo off
REM FSP Platform - Quick Start Script (Windows)

echo.
echo ===============================================================
echo 🚀 FSP (Future Scope Platform) - Quick Start
echo ===============================================================
echo.

REM Check Python
echo 📌 Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is required but not installed.
    exit /b 1
)
for /f "tokens=*" %%i in ('python --version') do echo ✅ %%i

REM Check Node
echo.
echo 📌 Checking Node.js...
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Node.js is required but not installed.
    exit /b 1
)
for /f "tokens=*" %%i in ('node --version') do echo ✅ Node %%i

REM Setup Backend
echo.
echo 📌 Setting up Backend...
cd backend

if not exist "venv" (
    echo    Creating virtual environment...
    python -m venv venv
)

echo    Activating virtual environment...
call venv\Scripts\activate.bat

echo    Installing dependencies...
pip install -r requirements.txt

echo    Creating .env file...
if not exist ".env" (
    copy .env.example .env
)

echo ✅ Backend setup complete

REM Setup Frontend
echo.
echo 📌 Setting up Frontend...
cd ..\frontend

echo    Installing dependencies...
call npm install

echo    Creating .env file...
if not exist ".env" (
    copy .env.example .env
)

echo ✅ Frontend setup complete

REM Initialize Database
echo.
echo 📌 Initializing Database...
cd ..
python init_db.py

echo.
echo ===============================================================
echo ✅ Setup Complete!
echo ===============================================================
echo.
echo 📌 To start the application:
echo.
echo Terminal 1 - Backend:
echo    cd backend
echo    venv\Scripts\activate
echo    uvicorn app.main:app --reload
echo.
echo Terminal 2 - Frontend:
echo    cd frontend
echo    npm run dev
echo.
echo 📌 URLs:
echo    • Frontend:  http://localhost:5173
echo    • Backend:   http://localhost:8000
echo    • API Docs:  http://localhost:8000/api/docs
echo.
echo ===============================================================
echo.
pause
