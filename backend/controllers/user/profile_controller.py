from flask import request, jsonify
from flask_login import current_user
from decorators.roles import user_required
from extensions import db

@user_required
def update_profile():

    data = request.get_json()

    current_user.full_name = data.get(
        "full_name",
        current_user.full_name
    )

    current_user.contact_number = data.get(
        "contact_number",
        current_user.contact_number
    )

    db.session.commit()

    return jsonify({
        "message":"Profile Updated"
    }),200
