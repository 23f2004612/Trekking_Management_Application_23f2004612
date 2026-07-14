import os
from werkzeug.security import generate_password_hash
from models.user import User
from extensions import db

def create_admin():

    admin = User.query.filter_by(email=os.environ.get("ADMIN_EMAIL")).first()

    if admin:
        return

    admin = User(
        full_name="Administrator",
        email=os.environ.get("ADMIN_EMAIL"),
        password=generate_password_hash(os.environ["ADMIN_PASSWORD"]),
        role="admin",
        status="active"
    )

    db.session.add(admin)
    db.session.commit()    