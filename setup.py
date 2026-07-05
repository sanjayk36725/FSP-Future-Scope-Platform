#!/usr/bin/env python
"""Startup script for FSP Platform"""

import os
import sys
import subprocess

def run_command(command, cwd=None):
    """Run a shell command"""
    print(f"\n▶️  Running: {command}")
    result = subprocess.run(command, shell=True, cwd=cwd)
    if result.returncode != 0:
        print(f"❌ Command failed: {command}")
        return False
    return True

def main():
    """Main startup function"""
    print("\n" + "="*50)
    print("🚀 FSP Platform Startup Script")
    print("="*50)
    
    # Get current directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    backend_dir = os.path.join(base_dir, "backend")
    
    print(f"\n📁 Project Directory: {base_dir}")
    
    # Step 1: Check Python
    print("\n📌 Step 1: Checking Python...")
    result = subprocess.run([sys.executable, "--version"], capture_output=True, text=True)
    print(f"   {result.stdout.strip()}")
    
    # Step 2: Setup Backend
    print("\n📌 Step 2: Setting up Backend...")
    
    # Create virtual environment if not exists
    venv_path = os.path.join(backend_dir, "venv")
    if not os.path.exists(venv_path):
        print("   Creating virtual environment...")
        run_command(f"{sys.executable} -m venv venv", cwd=backend_dir)
    
    # Determine activation command
    if sys.platform == "win32":
        activate_cmd = os.path.join(backend_dir, "venv", "Scripts", "activate.bat")
        pip_cmd = os.path.join(backend_dir, "venv", "Scripts", "pip")
    else:
        activate_cmd = f"source {os.path.join(backend_dir, 'venv', 'bin', 'activate')}"
        pip_cmd = os.path.join(backend_dir, "venv", "bin", "pip")
    
    print("   Installing backend dependencies...")
    run_command(f"{pip_cmd} install -r requirements.txt", cwd=backend_dir)
    
    # Initialize database
    print("   Initializing database...")
    run_command(f"{sys.executable} init_db.py", cwd=base_dir)
    
    # Step 3: Setup Frontend
    print("\n📌 Step 3: Setting up Frontend...")
    frontend_dir = os.path.join(base_dir, "frontend")
    print("   Installing frontend dependencies...")
    run_command("npm install", cwd=frontend_dir)
    
    # Step 4: Create env files
    print("\n📌 Step 4: Creating environment files...")
    
    backend_env = os.path.join(backend_dir, ".env")
    if not os.path.exists(backend_env):
        run_command(f"copy .env.example .env" if sys.platform == "win32" else "cp .env.example .env", cwd=backend_dir)
        print("   ✅ Created backend/.env")
    
    frontend_env = os.path.join(frontend_dir, ".env")
    if not os.path.exists(frontend_env):
        run_command(f"copy .env.example .env" if sys.platform == "win32" else "cp .env.example .env", cwd=frontend_dir)
        print("   ✅ Created frontend/.env")
    
    # Summary
    print("\n" + "="*50)
    print("✅ Setup Complete!")
    print("="*50)
    print("\n📌 Next Steps:")
    print("\n1️⃣  Backend (Terminal 1):")
    if sys.platform == "win32":
        print(f"   cd backend")
        print(f"   venv\\Scripts\\activate")
    else:
        print(f"   cd backend")
        print(f"   source venv/bin/activate")
    print(f"   uvicorn app.main:app --reload")
    
    print("\n2️⃣  Frontend (Terminal 2):")
    print(f"   cd frontend")
    print(f"   npm run dev")
    
    print("\n3️⃣  Access URLs:")
    print("   • Frontend: http://localhost:5173")
    print("   • Backend: http://localhost:8000")
    print("   • API Docs: http://localhost:8000/api/docs")
    
    print("\n" + "="*50)
    print("Happy Coding! 🚀")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()
