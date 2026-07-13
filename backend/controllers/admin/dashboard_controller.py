from flask import jsonify

from decorators.roles import admin_required

from models.user import User
from models.trek import Trek
from models.booking import Booking


@admin_required
def dashboard():

    return jsonify({

        "total_users":
            User.query.filter_by(role="user").count(),

        "total_staff":
            User.query.filter_by(role="staff").count(),

        "total_treks":
            Trek.query.count(),

        "total_bookings":
            Booking.query.count()

    }),200
