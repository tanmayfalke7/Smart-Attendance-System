from datetime import datetime

from sqlalchemy import (
    String, Integer, DateTime, Enum,
    Boolean, func
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class Camera(Base):
    __tablename__ = "cameras"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )

    device_code: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False
    )

    camera_type: Mapped[str] = mapped_column(
        Enum("ENTRY", "EXIT", name="camera_type"),
        nullable=False
    )

    location: Mapped[str] = mapped_column(
        String(150), nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )