from functools import wraps

from flask import jsonify

from flask_login import (
    current_user,
    login_required
)

def admin_required(func):

    @wraps(func)
    @login_required
    def wrapper(*args, **kwargs):

        if current_user.role != "admin":
            return jsonify({
                "message": "Admin access required"
            }), 403

        return func(*args, **kwargs)

    return wrapper

def staff_required(func):

    @wraps(func)
    @login_required
    def wrapper(*args, **kwargs):

        if current_user.role not in ["admin", "staff"]:
            return jsonify({
                "message": "Staff access required"
            }), 403

        return func(*args, **kwargs)

    return wrapper


def user_required(func):

    @wraps(func)
    @login_required
    def wrapper(*args, **kwargs):

        if current_user.role != "user":
            return jsonify({
                "message": "User access required"
            }), 403

        return func(*args, **kwargs)

    return wrapper

