from flask import request, jsonify
from flask_login import current_user
from decorators.roles import staff_required
from extensions import db
from models.trek import Trek
from schemas.trek_schema import treks_schema
from schemas.user_schema import users_schema
from utils.trek_utils import get_staff_trek_or_404
from services.redis_service import delete_cache

@staff_required
def my_treks():

    treks = Trek.query.filter_by(
        assigned_staff_id=current_user.id
    ).all()

    return treks_schema.dump(treks),200

@staff_required
def participants(trek_id):

    trek = get_staff_trek_or_404(trek_id)
    users = [
        booking.user
        for booking in trek.bookings
    ]

    return users_schema.dump(users),200

@staff_required
def update_trek(trek_id):

    trek = get_staff_trek_or_404(trek_id)
    data = request.get_json()

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"message": "Invalid or missing JSON body"}), 400

    trek.available_slots = data.get(
        "available_slots",
        trek.available_slots
    )

    allowed_status = {"Open", "Closed", "Completed"}

    if "status" in data and data["status"] not in allowed_status:
        return jsonify({"message": "Invalid status"}), 400

    trek.status = data.get(
        "status",
        trek.status
    )

    db.session.commit()

    delete_cache("available_treks")
    delete_cache(f"staff_dashboard_{current_user.id}")
    delete_cache("admin_dashboard")
    delete_cache("admin_treks")

    return jsonify({
        "message":"Updated"
    }),200

@staff_required
def complete_trek(trek_id):

    trek = get_staff_trek_or_404(trek_id)
    trek.status = "Completed"

    for booking in trek.bookings:
        if booking.booking_status != "Cancelled":
            booking.booking_status = "Completed"

    db.session.commit()

    delete_cache("available_treks")
    delete_cache(f"staff_dashboard_{current_user.id}")
    delete_cache("admin_dashboard")
    delete_cache("admin_treks")

    return jsonify({
        "message":"Trek Completed"
    }),200
