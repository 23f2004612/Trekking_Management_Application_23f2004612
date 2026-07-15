from flask import request, jsonify
from flask_login import current_user
from decorators.roles import user_required
from extensions import db
from models.user import User


@user_required
def get_profile():

    return jsonify({
        "id": current_user.id,
        "full_name": current_user.full_name,
        "email": current_user.email,
        "contact_number": current_user.contact_number
    }), 200


@user_required
def update_profile():

    data = request.get_json()

    full_name = data.get("full_name", "").strip()
    email = data.get("email", "").strip()
    contact = data.get("contact_number", "").strip()

    if not full_name:
        return jsonify({
            "message": "Full name is required."
        }), 400

    if not email:
        return jsonify({
            "message": "Email is required."
        }), 400

    existing = User.query.filter(
        User.email == email,
        User.id != current_user.id
    ).first()

    if existing:
        return jsonify({
            "message": "Email already exists."
        }), 400

    current_user.full_name = full_name
    current_user.email = email
    current_user.contact_number = contact

    db.session.commit()

    return jsonify({
        "message": "Profile updated successfully."
    }), 200