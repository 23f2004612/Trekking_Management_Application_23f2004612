from datetime import datetime
from extensions import db
from sqlalchemy import Enum

class Trek(db.Model):

    __tablename__ = "treks"

    id = db.Column(db.Integer, primary_key=True)

    trek_name = db.Column(
        db.String(100),
        nullable=False
    )

    location = db.Column(
        db.String(100),
        nullable=False
    )

    difficulty = db.Column(
        Enum(
            "Easy",
            "Moderate",
            "Hard",
            name="difficulty_levels"
        ),
        nullable=False
    )

    duration = db.Column(
        db.Integer,
        nullable=False
    )

    description = db.Column(db.Text)

    available_slots = db.Column(
        db.Integer,
        default=0
    )

    booked_slots = db.Column(
        db.Integer,
        default=0
    )

    start_date = db.Column(db.Date)

    end_date = db.Column(db.Date)

    status = db.Column(
        Enum(
            "Pending",
            "Approved",
            "Open",
            "Closed",
            "Completed",
            name="trek_status"
        ),
        nullable=False,
        default="Pending"
    )

    assigned_staff_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    staff = db.relationship(
        "User",
        back_populates="assigned_treks"
    )

    bookings = db.relationship(
        "Booking",
        back_populates="trek",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Trek {self.trek_name}>"