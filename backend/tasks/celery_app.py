from celery.schedules import crontab

from application import create_app
from extensions import celery

# Create a Flask app WITHOUT running startup logic
flask_app = create_app(init_admin=False)

# Configure Celery once
celery.conf.broker_url = flask_app.config["CELERY_BROKER_URL"]
celery.conf.result_backend = flask_app.config["CELERY_RESULT_BACKEND"]

class FlaskTask(celery.Task):
    abstract = True

    def __call__(self, *args, **kwargs):
        with flask_app.app_context():
            return self.run(*args, **kwargs)

celery.Task = FlaskTask

celery.conf.beat_schedule = {
    "daily-reminder": {
        "task": "tasks.reminder_tasks.send_daily_reminders",
        "schedule": crontab(hour=9, minute=0),
    },
    "monthly-report": {
        "task": "tasks.report_tasks.monthly_report",
        "schedule": crontab(day_of_month=1, hour=10, minute=0),
    },
}

import tasks.booking_tasks
import tasks.reminder_tasks
import tasks.report_tasks