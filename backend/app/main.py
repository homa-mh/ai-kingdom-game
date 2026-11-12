
from fastapi import FastAPI

from app.api.citizens import router as citizens_router
from app.api.kingdoms import router as kingdoms_router
from app.database import Base, engine
from app.models.citizen import Citizen
from app.models.kingdom import Kingdom

# ایجاد جدول‌های دیتابیس
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Kingdom API",
    description="Backend API for the AI Kingdom game",
    version="0.1.0",
)

app.include_router(kingdoms_router)
app.include_router(citizens_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to AI Kingdom!",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }
