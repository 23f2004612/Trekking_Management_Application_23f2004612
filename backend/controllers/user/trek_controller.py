from flask import jsonify
from decorators.roles import user_required
from models.trek import Trek
from schemas.trek_schema import treks_schema, trek_schema
from services.redis_service import (
    get_cache,
    set_cache
)
from flask_login import current_user

def available_treks():

    treks = Trek.query.filter_by(
        status="Open"
    ).order_by(
        Trek.start_date
    ).all()

    result = treks_schema.dump(treks)

    booked = set()

    if current_user.is_authenticated:

        booked = {
            booking.trek_id
            for booking in current_user.bookings
            if booking.booking_status == "Booked"
        }

    for trek in result:

        trek["already_booked"] = (
            trek["id"] in booked
        )

    return jsonify({
        "success": True,
        "treks": result,
        "message": (
            "No treks available at the moment."
            if not result
            else None
        )
    }), 200 

def trek_details(trek_id):
    trek = Trek.query.get_or_404(trek_id)
    return trek_schema.dump(trek),200

