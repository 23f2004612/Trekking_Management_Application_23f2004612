import os
from flask import jsonify, send_file
from flask_login import current_user
from decorators.roles import user_required
from extensions import db
from models.booking import Booking
from models.trek import Trek
from utils.booking_utils import get_user_booking_or_404
from schemas.booking_schema import bookings_schema
from services.redis_service import delete_cache
from celery.result import AsyncResult

@user_required
def book_trek(trek_id):

    trek = Trek.query.get_or_404(trek_id)

    if trek.status != "Open":

        return jsonify({
            "message":"Trek Closed"
        }),400

    if trek.booked_slots >= trek.available_slots:

        return jsonify({
            "message":"No Slots Available"
        }),400

    booking = Booking.query.filter_by(

        user_id=current_user.id,

        trek_id=trek.id

    ).first()

    if booking and booking.booking_status != "Cancelled":

        return jsonify({
            "message":"Already Booked"
        }),400

    booking = Booking(
        user_id=current_user.id,
        trek_id=trek.id
    )

    trek.booked_slots += 1

    db.session.add(booking)

    db.session.commit()

    delete_cache("available_treks")
    delete_cache("admin_dashboard")
    delete_cache(f"staff_dashboard_{trek.assigned_staff_id}")

    return jsonify({
        "message":"Booking Successful"
    }),201

@user_required
def cancel_booking(booking_id):

    booking = get_user_booking_or_404(
        booking_id
    )

    if booking.booking_status == "Cancelled":
        return jsonify({
            "message": "Booking already cancelled"
        }), 400

    booking.booking_status = "Cancelled"

    booking.trek.booked_slots -= 1

    db.session.commit()

    delete_cache("available_treks")
    delete_cache("admin_dashboard")
    delete_cache(f"staff_dashboard_{booking.trek.assigned_staff_id}")
    
    return jsonify({
        "message":"Booking Cancelled"
    }),200

@user_required
def booking_history():

    bookings = Booking.query.filter_by(
        user_id=current_user.id
    ).all()

    return bookings_schema.dump(bookings),200

@user_required
def export_history():

    from tasks.booking_tasks import export_booking_history
    
    task = export_booking_history.delay(
        current_user.id
    )

    set_cache(f"export_owner_{task.id}", current_user.id)
    return jsonify({
        "message": "Export started",
        "task_id": task.id
    }), 202

@user_required
def get_export_status(task_id):

    owner_id = get_cache(f"export_owner_{task_id}")
    if owner_id != current_user.id:
        return jsonify({"message": "Not found"}), 404
        
    task = AsyncResult(task_id)
    
    if task.state == "PENDING":

        return jsonify({
            "status": "PENDING",
            "message": "Export is queued"
        }), 202

    if task.state == "STARTED":

        return jsonify({
            "status": "STARTED",
            "message": "Export is being generated"
        }), 202

    if task.state == "FAILURE":

        return jsonify({
            "status": "FAILURE",
            "message": "Export failed"
        }), 500

    if task.state == "SUCCESS":

        filename = task.result

        if not os.path.exists(filename):

            return jsonify({
                "status": "FAILURE",
                "message": "File not found"
            }),404

        return send_file(

            filename,

            as_attachment=True,

            download_name=os.path.basename(filename),

            mimetype="text/csv"

        )

    return jsonify({
        "status": task.state
    }),200