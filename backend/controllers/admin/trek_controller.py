from flask import jsonify
from decorators.roles import admin_required
from models.trek import Trek
from schemas.trek_schema import treks_schema
from flask import request
from datetime import datetime
from models.user import User
from extensions import db

@admin_required
def get_treks():

    treks = Trek.query.order_by(
        Trek.start_date
    ).all()

    return treks_schema.dump(treks), 200

@admin_required
def create_trek():

    data = request.get_json()

    required = ["trek_name", "location", "difficulty", "duration",
                "description", "available_slots", "start_date",
                "end_date", "assigned_staff_id"]
    missing = [f for f in required if f not in data]
    if missing:
        return jsonify({"message": f"Missing fields: {missing}"}), 400

    staff = User.query.filter_by(
        id=data["assigned_staff_id"],
        role="staff",
        status="active"
    ).first()

    if not staff:
        return jsonify({
            "message": "Invalid Staff"
        }),404

    try:
        start_date = datetime.strptime(data["start_date"], "%Y-%m-%d").date()
        end_date = datetime.strptime(data["end_date"], "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return jsonify({"message": "Invalid date format"}), 400

    if end_date <= start_date:
        return jsonify({"message": "end_date must be after start_date"}), 400

    trek = Trek(

        trek_name=data["trek_name"],

        location=data["location"],

        difficulty=data["difficulty"],

        duration=data["duration"],

        description=data["description"],

        available_slots=data["available_slots"],

        booked_slots=0,

        start_date=start_date,

        end_date=end_date,

        status="Open",

        assigned_staff_id=data["assigned_staff_id"]

    )

    db.session.add(trek)

    db.session.commit()

    return jsonify({
        "message":"Trek Created"
    }),201

@admin_required
def update_trek(trek_id):

    trek = Trek.query.get_or_404(trek_id)

    data = request.get_json()

    trek.trek_name = data.get(
        "trek_name",
        trek.trek_name
    )

    trek.location = data.get(
        "location",
        trek.location
    )

    trek.description = data.get(
        "description",
        trek.description
    )

    trek.available_slots = data.get(
        "available_slots",
        trek.available_slots
    )

    if trek.available_slots < trek.booked_slots:
        return jsonify({
            "message": "available_slots cannot be less than booked_slots"
        }), 400    

    trek.duration = data.get(
        "duration",
        trek.duration
    )

    trek.difficulty = data.get(
        "difficulty",
        trek.difficulty
    )

    if "assigned_staff_id" in data:

        staff = User.query.filter_by(
            id=data["assigned_staff_id"],
            role="staff",
            status="active"
        ).first()

        if not staff:
            return jsonify({
                "message":"Invalid Staff"
            }),404

        trek.assigned_staff_id = data["assigned_staff_id"]

    db.session.commit()

    return jsonify({
        "message":"Updated Successfully"
    }),200

@admin_required
def delete_trek(trek_id):

    trek = Trek.query.get_or_404(trek_id)

    trek.status = "Closed"

    db.session.commit()

    return jsonify({
        "message":"Trek Closed"
    }),200

