from flask import abort
from flask_login import current_user
from models.booking import Booking

def get_user_booking_or_404(booking_id):

    booking = Booking.query.get_or_404(booking_id)

    if booking.user_id != current_user.id:
        abort(403, description="Unauthorized")

    return booking
