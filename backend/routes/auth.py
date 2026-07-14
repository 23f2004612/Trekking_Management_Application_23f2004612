from flask import Blueprint, request, jsonify
from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from models.user import User
from extensions import db
from sqlalchemy.exc import IntegrityError

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/api"
)

@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json(silent=True) or {}

    name = data.get("full_name")
    email = data.get("email")
    password = data.get("password")
    phone = data.get("contact_number")

    if not all([name, email, password]):
        return jsonify({"message": "Missing required fields"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({
            "message": "Email already exists"
        }), 400

    user = User(
        full_name=name,
        email=email,
        password=generate_password_hash(password),
        contact_number=phone,
        role="user"
    )

    db.session.add(user)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({
            "message": "Registration failed"
        }), 400

    return jsonify({
        "message": "Registration successful"
    }), 201

@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()
    
    if not user:
        return jsonify({
            "message": "Invalid Credentials"
        }), 401

    if not check_password_hash(user.password, password):
        return jsonify({
            "message": "Invalid Credentials"
        }), 401

    if user.status == "blacklisted":
        return jsonify({
            "message": "Account Disabled"
        }), 403

    login_user(user, remember=True)

    return jsonify({
        "message": "Login Successful",
        "id": user.id,
        "role": user.role,
        "user_id": user.id,
        "name": user.full_name,
        "full_name": user.full_name,
        "email": user.email
    }), 200

@auth_bp.route("/logout", methods=["POST"])
@login_required
def logout():

    logout_user()
    return jsonify({
        "message": "Logged Out"
    }), 200

@auth_bp.route("/me", methods=["GET"])
@login_required
def me():
    return jsonify({
        "id": current_user.id,
        "name": current_user.full_name,
        "full_name": current_user.full_name,
        "email": current_user.email,
        "role": current_user.role
    })