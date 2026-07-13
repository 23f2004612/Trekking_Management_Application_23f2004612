from flask import jsonify
from flask_login import current_user
from decorators.roles import user_required
from models.booking import Booking
from models.trek import Trek

@user_required
def dashboard():

    total_bookings = Booking.query.filter_by(
        user_id=current_user.id
    ).count()

    available_treks = Trek.query.filter_by(
        status="Open"
    ).count()

    return jsonify({
        "available_treks": available_treks,
        "my_bookings": total_bookings
    }),200
