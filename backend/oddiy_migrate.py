from app.db.database import engine
from app.models.models import Base

def create_tables():
    print("Jadvallar yaratilmoqda...")
    Base.metadata.create_all(bind=engine)
    print("Jadvallar muvaffaqiyatli yaratildi!")

if __name__ == "__main__":
    create_tables()