from flask import jsonify

from decorators.roles import admin_required

from models.user import User
from models.trek import Trek
from models.booking import Booking
from services.redis_service import (
    get_cache,
    set_cache
)

@admin_required
def dashboard():

    cache_key = "admin_dashboard"

    cached = get_cache(cache_key)

    if cached:
        return cached, 200

    result = {

        "total_users":
            User.query.filter_by(role="user").count(),

        "total_staff":
            User.query.filter_by(role="staff").count(),

        "total_treks":
            Trek.query.count(),

        "total_bookings":
            Booking.query.count()

    }
    set_cache(cache_key, result)
    return result, 200