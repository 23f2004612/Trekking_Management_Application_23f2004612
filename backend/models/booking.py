from datetime import datetime
from extensions import db
from sqlalchemy import Enum

class Booking(db.Model):

    __tablename__ = "bookings"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    trek_id = db.Column(
        db.Integer,
        db.ForeignKey("treks.id"),
        nullable=False
    )

    booking_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    booking_status = db.Column(
        Enum(
            "Booked",
            "Cancelled",
            "Completed",
            name="booking_status"
        ),
        nullable=False,
        default="Booked"
    )

    remarks = db.Column(db.String(255))

    user = db.relationship(
        "User",
        back_populates="bookings"
    )

    trek = db.relationship(
        "Trek",
        back_populates="bookings"
    )

    __table_args__ = (
        db.UniqueConstraint(
            "user_id",
            "trek_id",
            name="unique_booking"
        ),
    )

    def __repr__(self):
        return f"<Booking {self.id}>"