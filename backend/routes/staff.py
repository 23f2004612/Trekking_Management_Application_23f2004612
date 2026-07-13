from flask import Blueprint

from controllers.staff.dashboard_controller import dashboard
from controllers.staff.trek_controller import (
    my_treks,
    participants,
    update_trek,
    complete_trek
)

staff_bp = Blueprint(
    "staff",
    __name__,
    url_prefix="/api/staff"
)

staff_bp.add_url_rule(
    "/dashboard",
    view_func=dashboard,
    methods=["GET"]
)

staff_bp.add_url_rule(
    "/my-treks",
    view_func=my_treks,
    methods=["GET"]
)

staff_bp.add_url_rule(
    "/treks/<int:trek_id>/participants",
    view_func=participants,
    methods=["GET"]
)

staff_bp.add_url_rule(
    "/treks/<int:trek_id>",
    view_func=update_trek,
    methods=["PUT"]
)

staff_bp.add_url_rule(
    "/treks/<int:trek_id>/complete",
    view_func=complete_trek,
    methods=["PUT"]
)