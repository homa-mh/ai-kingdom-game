
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# مسیر فایل دیتابیس
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_URL = f"sqlite:///{BASE_DIR / 'kingdom.db'}"

# ایجاد اتصال به SQLite
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# ساخت Session برای ارتباط با دیتابیس
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

# کلاس پایه تمام مدل‌های دیتابیس
class Base(DeclarativeBase):
    pass


# وابستگی دیتابیس برای استفاده در API
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
