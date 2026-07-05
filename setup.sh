#!/bin/bash
# FSP Platform - Quick Start Script (macOS/Linux)

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "🚀 FSP (Future Scope Platform) - Quick Start"
echo "═══════════════════════════════════════════════════════════════"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Python
echo "📌 Checking Python..."
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 is required but not installed.${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Python $(python3 --version)${NC}"

# Check Node
echo ""
echo "📌 Checking Node.js..."
if ! command -v node &> /dev/null; then
    echo -e "${RED}❌ Node.js is required but not installed.${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Node $(node --version)${NC}"

# Setup Backend
echo ""
echo "📌 Setting up Backend..."
cd backend

if [ ! -d "venv" ]; then
    echo "   Creating virtual environment..."
    python3 -m venv venv
fi

echo "   Activating virtual environment..."
source venv/bin/activate

echo "   Installing dependencies..."
pip install -r requirements.txt

echo "   Creating .env file..."
if [ ! -f ".env" ]; then
    cp .env.example .env
fi

echo -e "${GREEN}✅ Backend setup complete${NC}"

# Setup Frontend
echo ""
echo "📌 Setting up Frontend..."
cd ../frontend

echo "   Installing dependencies..."
npm install

echo "   Creating .env file..."
if [ ! -f ".env" ]; then
    cp .env.example .env
fi

echo -e "${GREEN}✅ Frontend setup complete${NC}"

# Initialize Database
echo ""
echo "📌 Initializing Database..."
cd ..
python3 init_db.py

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo -e "${GREEN}✅ Setup Complete!${NC}"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "📌 To start the application:"
echo ""
echo -e "${YELLOW}Terminal 1 - Backend:${NC}"
echo "  cd backend"
echo "  source venv/bin/activate"
echo "  uvicorn app.main:app --reload"
echo ""
echo -e "${YELLOW}Terminal 2 - Frontend:${NC}"
echo "  cd frontend"
echo "  npm run dev"
echo ""
echo "📌 URLs:"
echo "   • Frontend:  http://localhost:5173"
echo "   • Backend:   http://localhost:8000"
echo "   • API Docs:  http://localhost:8000/api/docs"
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo ""
