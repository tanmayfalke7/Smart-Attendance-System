from datetime import date, time, datetime

from sqlalchemy import (
    String, Integer, Time, Date, DateTime,
    ForeignKey, Boolean, UniqueConstraint, func
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class Shift(Base):
    __tablename__ = "shifts"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(80), unique=True, nullable=False
    )

    start_time: Mapped[time] = mapped_column(
        Time, nullable=False
    )

    end_time: Mapped[time] = mapped_column(
        Time, nullable=False
    )

    # Expected net working duration, excluding unpaid breaks.
    scheduled_minutes: Mapped[int] = mapped_column(
        Integer, nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False
    )


class ShiftAssignment(Base):
    __tablename__ = "shift_assignments"

    __table_args__ = (
        UniqueConstraint(
            "employee_id",
            "work_date",
            name="uq_employee_shift_work_date"
        ),
    )

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )

    employee_id: Mapped[int] = mapped_column(
        ForeignKey("employees.id"), nullable=False, index=True
    )

    shift_id: Mapped[int] = mapped_column(
        ForeignKey("shifts.id"), nullable=False
    )

    # Date on which the assigned shift starts.
    work_date: Mapped[date] = mapped_column(
        Date, nullable=False, index=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )