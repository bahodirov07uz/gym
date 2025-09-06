import asyncio
from app.db.database import SessionLocal
from app.models.models import User, UserRole
from app.utils.responses import Hasher

def create_admin():
    db = SessionLocal()
    hashed_pw = Hasher.get_password_hash("admin123")
    admin = User(
        username="admin",
        email="admin@example.com",
        hashed_password=hashed_pw,
        role=UserRole.ADMIN
    )
    db.add(admin)
    db.commit()
    db.refresh(admin)
    print("✅ Admin user created:", admin.username)

if __name__ == "__main__":
    create_admin()
