from fastapi import FastAPI
from sqlalchemy import text

from app.core.config import settings
from app.db.session import engine


app = FastAPI(
    title=settings.APP_NAME,
    description="Office attendance management API",
    version="0.1.0",
    debug=settings.DEBUG
)


@app.get("/", tags=["General"])
def root():
    return {
        "message": "Smart Office Attendance API is running",
        "environment": settings.APP_ENV
    }


@app.get("/health/live", tags=["Health"])
def health_live():
    # Confirms that the API process is alive.
    return {"status": "alive"}


@app.get("/health/ready", tags=["Health"])
def health_ready():
    # Confirms that the API can communicate with MySQL.
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "ready",
            "database": "connected"
        }

    except Exception:
        return {
            "status": "not_ready",
            "database": "disconnected"
        }