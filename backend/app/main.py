
from fastapi import FastAPI

app = FastAPI(
    title="AI Kingdom API",
    description="Backend API for the AI Kingdom game",
    version="0.1.0",
)


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
