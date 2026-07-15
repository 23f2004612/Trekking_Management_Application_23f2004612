from flask import Blueprint

# Dashboard
from controllers.user.dashboard_controller import dashboard

# Trek
from controllers.user.trek_controller import (
    available_treks,
    trek_details
)

# Booking
from controllers.user.booking_controller import (
    book_trek,
    cancel_booking,
    booking_history,
    export_history,
    get_export_status
)

# Profile
from controllers.user.profile_controller import (update_profile, get_profile)

from controllers.user.search_controller import (
    search_treks
)
from controllers.user.booking_controller import download_export

user_bp = Blueprint(
    "user",
    __name__,
    url_prefix="/api/user"
)

# Dashboard
user_bp.add_url_rule(
    "/dashboard",
    view_func=dashboard,
    methods=["GET"]
)

# Trek APIs
user_bp.add_url_rule(
    "/treks",
    view_func=available_treks,
    methods=["GET"]
)

user_bp.add_url_rule(
    "/treks/<int:trek_id>",
    view_func=trek_details,
    methods=["GET"]
)

# Booking APIs
user_bp.add_url_rule(
    "/book/<int:trek_id>",
    view_func=book_trek,
    methods=["POST"]
)

user_bp.add_url_rule(
    "/booking/<int:booking_id>",
    view_func=cancel_booking,
    methods=["DELETE"]
)

user_bp.add_url_rule(
    "/history",
    view_func=booking_history,
    methods=["GET"]
)

# Profile API
user_bp.add_url_rule(
    "/profile",
    view_func=get_profile,
    methods=["GET"]
)

user_bp.add_url_rule(
    "/profile",
    view_func=update_profile,
    methods=["PUT"]
)

#Search API
user_bp.add_url_rule(
    "/search",
    view_func=search_treks,
    methods=["GET"]
)

user_bp.add_url_rule(
    "/history/export",
    view_func=export_history,
    methods=["POST"]
)

user_bp.add_url_rule(
    "/export/<task_id>",
    view_func=get_export_status,
    methods=["GET"]
)

user_bp.add_url_rule(
    "/download",
    view_func=download_export,
    methods=["GET"]
)