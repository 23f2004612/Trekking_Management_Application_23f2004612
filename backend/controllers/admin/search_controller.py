from flask import request
from sqlalchemy import or_
from decorators.roles import admin_required
from models.user import User
from models.trek import Trek
from schemas.user_schema import users_schema
from schemas.trek_schema import treks_schema

@admin_required
def search_users():

    q = request.args.get("q", "").strip()

    users = User.query.filter(
        User.role == "user",
        or_(
            User.full_name.ilike(f"%{q}%"),
            User.email.ilike(f"%{q}%"),
            User.contact_number.ilike(f"%{q}%")
        )
    ).all()

    return users_schema.dump(users), 200

@admin_required
def search_staff():

    q = request.args.get("q", "").strip()

    staff = User.query.filter(
        User.role == "staff",
        or_(
            User.full_name.ilike(f"%{q}%"),
            User.email.ilike(f"%{q}%"),
            User.specialization.ilike(f"%{q}%")
        )
    ).all()

    return users_schema.dump(staff), 200

@admin_required
def search_treks():

    q = request.args.get("q", "").strip()

    treks = Trek.query.filter(
        or_(
            Trek.trek_name.ilike(f"%{q}%"),
            Trek.location.ilike(f"%{q}%"),
            Trek.difficulty.ilike(f"%{q}%")
        )
    ).all()

    return treks_schema.dump(treks), 200
