from flask import Blueprint

from controllers.admin.dashboard_controller import *
from controllers.admin.user_controller import *
from controllers.admin.staff_controller import *
from controllers.admin.trek_controller import *

admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/api/admin"
)

# Dashboard
admin_bp.add_url_rule(
    "/dashboard",
    view_func=dashboard,
    methods=["GET"]
)

# Users
admin_bp.add_url_rule(
    "/users",
    view_func=get_users,
    methods=["GET"]
)

admin_bp.add_url_rule(
    "/users/<int:user_id>/status",
    view_func=update_user_status,
    methods=["PUT"]
)

# Staff
admin_bp.add_url_rule(
    "/staff",
    view_func=get_staff,
    methods=["GET"]
)

admin_bp.add_url_rule(
    "/staff",
    view_func=create_staff,
    methods=["POST"]
)

admin_bp.add_url_rule(
    "/staff/<int:staff_id>",
    view_func=update_staff,
    methods=["PUT"]
)

admin_bp.add_url_rule(
    "/staff/<int:staff_id>",
    view_func=delete_staff,
    methods=["DELETE"]
)

#Trek
admin_bp.add_url_rule(
    "/treks",
    view_func=get_treks,
    methods=["GET"]
)

admin_bp.add_url_rule(
    "/treks",
    view_func=create_trek,
    methods=["POST"]
)

admin_bp.add_url_rule(
    "/treks/<int:trek_id>",
    view_func=update_trek,
    methods=["PUT"]
)

admin_bp.add_url_rule(
    "/treks/<int:trek_id>",
    view_func=delete_trek,
    methods=["DELETE"]
)

