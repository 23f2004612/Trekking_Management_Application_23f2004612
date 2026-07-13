from flask import abort
from flask_login import current_user
from models.trek import Trek

def get_staff_trek_or_404(trek_id):

    trek = Trek.query.get_or_404(trek_id)

    if trek.assigned_staff_id != current_user.id:
        abort(403, description="Unauthorized")

    return trek
