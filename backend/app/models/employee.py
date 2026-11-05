from datetime import datetime

from sqlalchemy import (
    String, Integer, DateTime, Enum, Boolean,
    func
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True
    )

    employee_code: Mapped[str] = mapped_column(
        String(30), unique=True, nullable=False, index=True
    )

    full_name: Mapped[str] = mapped_column(
        String(120), nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(150), unique=True, nullable=False
    )

    department: Mapped[str | None] = mapped_column(
        String(100), nullable=True
    )

    designation: Mapped[str | None] = mapped_column(
        String(100), nullable=True
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )