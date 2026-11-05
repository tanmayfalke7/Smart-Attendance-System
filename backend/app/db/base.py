from app.db.session import Base

# Import all models so SQLAlchemy metadata discovers them.
from app.models.employee import Employee
from app.models.shift import Shift, ShiftAssignment
from app.models.camera import Camera
from app.models.attendance import (
    AttendanceEvent,
    AttendanceSession,
    DailyAttendance
)