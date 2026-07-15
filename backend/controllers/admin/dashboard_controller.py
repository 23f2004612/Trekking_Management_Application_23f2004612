from flask import jsonify
from sqlalchemy import func, extract
from decorators.roles import admin_required
from extensions import db
from models.user import User
from models.trek import Trek
from models.booking import Booking

from services.redis_service import get_cache, set_cache

@admin_required
def dashboard():

    cache_key = "admin_dashboard"

    cached = get_cache(cache_key)

    if cached is not None:
        return jsonify(cached), 200

    total_treks = Trek.query.count()

    total_users = User.query.filter_by(role="user").count()

    total_staff = User.query.filter_by(role="staff").count()

    total_bookings = Booking.query.count()

    difficulty_distribution = {
        "Easy": Trek.query.filter_by(difficulty="Easy").count(),
        "Moderate": Trek.query.filter_by(difficulty="Moderate").count(),
        "Hard": Trek.query.filter_by(difficulty="Hard").count(),
    }

    monthly_bookings = {
        "Jan": 0,
        "Feb": 0,
        "Mar": 0,
        "Apr": 0,
        "May": 0,
        "Jun": 0,
        "Jul": 0,
        "Aug": 0,
        "Sep": 0,
        "Oct": 0,
        "Nov": 0,
        "Dec": 0,
    }

    rows = (
        db.session.query(
            extract("month", Booking.booking_date),
            func.count(Booking.id),
        )
        .group_by(extract("month", Booking.booking_date))
        .all()
    )

    months = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    for month, count in rows:

        if month is not None:
            monthly_bookings[months[int(month) - 1]] = count

    result = {
        "total_treks": total_treks,
        "total_users": total_users,
        "total_staff": total_staff,
        "total_bookings": total_bookings,
        "difficulty_distribution": difficulty_distribution,
        "monthly_bookings": monthly_bookings,
    }

    set_cache(cache_key, result)
    return jsonify(result), 200