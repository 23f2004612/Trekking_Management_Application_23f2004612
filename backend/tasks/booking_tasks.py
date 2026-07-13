import csv
import os
from extensions import celery
from models.booking import Booking
from datetime import datetime

@celery.task
def export_booking_history(user_id):

    bookings = Booking.query.filter_by(
        user_id=user_id
    ).all()

    folder = "exports"

    os.makedirs(folder, exist_ok=True)

    filename = (
        f"exports/user_{user_id}_"
        f"{datetime.now():%Y%m%d_%H%M%S}.csv"
    )

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Booking ID",
            "Trek",
            "Location",
            "Status",
            "Booking Date"
        ])

        for booking in bookings:

            writer.writerow([
                booking.id,
                booking.trek.trek_name,
                booking.trek.location,
                booking.booking_status,
                booking.booking_date
            ])

    return filename

