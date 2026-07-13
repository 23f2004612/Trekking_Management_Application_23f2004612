from flask import jsonify
from flask_login import current_user
from decorators.roles import staff_required

from models.trek import Trek
from models.booking import Booking
from services.redis_service import (
    get_cache,
    set_cache
)

@staff_required
def dashboard():

    cache_key = f"staff_dashboard_{current_user.id}"

    cached = get_cache(cache_key)

    if cached:
        return cached, 200

    result = {

        "assigned_treks":

            Trek.query.filter_by(
                assigned_staff_id=current_user.id
            ).count(),

        "total_bookings":

            Booking.query.join(Trek).filter(
                Trek.assigned_staff_id == current_user.id
            ).count()

    }

    set_cache(cache_key, result)
    return result, 200
