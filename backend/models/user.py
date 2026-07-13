from datetime import datetime
from extensions import db
from flask_login import UserMixin
from sqlalchemy import Enum

class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(100), nullable=False)

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password = db.Column(db.String(255), nullable=False)

    contact_number = db.Column(db.String(15))

    role = db.Column(
        Enum("admin", "staff", "user", name="user_roles"),
        nullable=False,
        default="user"
    )

    status = db.Column(
        Enum("active", "blacklisted", name="user_status"),
        nullable=False,
        default="active"
    )

    specialization = db.Column(db.String(100))

    experience = db.Column(db.Integer)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    bookings = db.relationship(
        "Booking",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    assigned_treks = db.relationship(
        "Trek",
        back_populates="staff"
    )

    def __repr__(self):
        return f"<User {self.email}>"
