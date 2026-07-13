from datetime import datetime
from extensions import celery

from models.user import User
from models.trek import Trek
from models.booking import Booking

@celery.task
def monthly_report():

    report = {

        "generated_at":
            datetime.now().strftime("%d-%m-%Y"),

        "total_users":
            User.query.filter_by(
                role="user"
            ).count(),

        "total_staff":
            User.query.filter_by(
                role="staff"
            ).count(),

        "total_treks": Trek.query.count(),

        "total_bookings": Booking.query.count(),

        "completed_treks":
            Trek.query.filter_by(
                status="Completed"
            ).count()
    }

    print(report)
    return report
