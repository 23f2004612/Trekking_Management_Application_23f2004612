from flask import request, jsonify
from werkzeug.security import generate_password_hash
from decorators.roles import admin_required
from models.user import User
from extensions import db
from schemas.user_schema import users_schema
from sqlalchemy.exc import IntegrityError

@admin_required
def get_staff():

    staff = User.query.filter_by(
        role="staff"
    ).all()

    return users_schema.dump(staff),200

@admin_required
def create_staff():

    data = request.get_json()

    required = ["full_name", "email", "password", "contact_number",
                "specialization", "experience"]
    missing = [f for f in required if f not in data]
    if missing:
        return jsonify({"message": f"Missing fields: {missing}"}), 400

    if User.query.filter_by(
        email=data["email"]
    ).first():

        return jsonify({

            "message":"Email already exists"

        }),400

    staff = User(

        full_name=data["full_name"],

        email=data["email"],

        password=generate_password_hash(
            data["password"]
        ),

        contact_number=data["contact_number"],

        specialization=data["specialization"],

        experience=data["experience"],

        role="staff",

        status="active"

    )

    db.session.add(staff)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Email already exists"}), 400

    return jsonify({

        "message":"Staff Created"

    }),201
        
@admin_required
def update_staff(staff_id):

    staff = User.query.get_or_404(staff_id)

    if staff.role != "staff":

        return jsonify({

            "message":"Invalid Staff"

        }),404

    data = request.get_json()

    staff.full_name = data.get(
        "full_name",
        staff.full_name
    )

    staff.contact_number = data.get(
        "contact_number",
        staff.contact_number
    )

    staff.specialization = data.get(
        "specialization",
        staff.specialization
    )

    staff.experience = data.get(
        "experience",
        staff.experience
    )

    db.session.commit()

    return jsonify({

        "message":"Updated"

    }),200

@admin_required
def delete_staff(staff_id):

    staff = User.query.get_or_404(staff_id)

    if staff.role != "staff":

        return jsonify({

            "message":"Invalid Staff"

        }),404

    staff.status = "blacklisted"

    db.session.commit()

    return jsonify({

        "message":"Staff Deactivated"

    }),200

