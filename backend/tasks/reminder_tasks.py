from datetime import date, timedelta
from extensions import celery
from models.trek import Trek

@celery.task
def send_daily_reminders():

    tomorrow = date.today() + timedelta(days=1)

    treks = Trek.query.filter(
        Trek.start_date == tomorrow,
        Trek.status == "Open"
    ).all()

    reminders = []

    for trek in treks:
        for booking in trek.bookings:

            reminders.append({

                "email": booking.user.email,

                "message": f"""
                    Hi {booking.user.full_name},

                    Reminder!

                    Your trek "{trek.trek_name}"
                    starts tomorrow.

                    Location: {trek.location}

                    Have a great trek!
                    """
            })

            print(
                f"Reminder sent to "
                f"{booking.user.email}"
            )

    return reminders