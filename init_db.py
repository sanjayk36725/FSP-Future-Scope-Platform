import sys
import os

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from app.db.database import init_db, SessionLocal
from app.models.user import Role, Permission

def init_database():
    """Initialize database with tables and default data"""
    try:
        # Create all tables
        init_db()
        print("✅ Database tables created successfully")
        
        # Create default roles
        db = SessionLocal()
        
        roles_data = [
            ("student", "Student role - for learners"),
            ("faculty", "Faculty role - for teachers"),
            ("developer", "Developer role - for software developers"),
            ("recruiter", "Recruiter role - for recruitment professionals"),
            ("hr_manager", "HR Manager role - for HR operations"),
            ("administrator", "Administrator role - for system admins"),
        ]
        
        for role_name, description in roles_data:
            existing = db.query(Role).filter(Role.name == role_name).first()
            if not existing:
                role = Role(name=role_name, description=description)
                db.add(role)
                print(f"✅ Created role: {role_name}")
        
        db.commit()
        
        # Create default permissions
        permissions_data = [
            ("view_dashboard", "view_dashboard", "View Dashboard"),
            ("view_profile", "view_profile", "View Profile"),
            ("edit_profile", "edit_profile", "Edit Profile"),
            ("manage_users", "manage_users", "Manage Users"),
            ("manage_roles", "manage_roles", "Manage Roles"),
            ("manage_system", "manage_system", "Manage System"),
        ]
        
        for code, code_value, name in permissions_data:
            existing = db.query(Permission).filter(Permission.code == code).first()
            if not existing:
                permission = Permission(name=name, code=code_value)
                db.add(permission)
                print(f"✅ Created permission: {name}")
        
        db.commit()
        db.close()
        
        print("\n✅ Database initialization completed successfully!")
        print("\n📌 You can now:")
        print("   1. Start backend: cd backend && uvicorn app.main:app --reload")
        print("   2. Start frontend: cd frontend && npm run dev")
        print("   3. Visit: http://localhost:8000/api/docs for API documentation")
        print("   4. Visit: http://localhost:5173 for frontend")
        
    except Exception as e:
        print(f"❌ Error initializing database: {str(e)}")
        raise

if __name__ == "__main__":
    init_database()
