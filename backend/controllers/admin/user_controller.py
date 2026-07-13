from flask import jsonify
from decorators.roles import admin_required
from models.user import User
from extensions import db
from schemas.user_schema import users_schema

@admin_required
def get_users():

    users = User.query.filter_by(
        role="user"
    ).all()

    return users_schema.dump(users),200

@admin_required
def update_user_status(user_id):

    user = User.query.get_or_404(user_id)
    if user.role != "user":

        return jsonify({
            "message":"This endpoint only manages regular user accounts"
        }),400

    user.status = (
        "active"
        if user.status == "blacklisted"
        else "blacklisted"
    )
    db.session.commit()

    return jsonify({
        "message":"Status Updated",
        "status":user.status
    }),200

