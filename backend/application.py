from flask import Flask, jsonify
from config import Config
from extensions import db, migrate, login_manager, ma

from models import User
from services.admin_initializer import create_admin

from routes.auth import auth_bp
from routes.admin import admin_bp
from routes.staff import staff_bp
from routes.user import user_bp


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def create_app(init_admin=True):

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(staff_bp)
    app.register_blueprint(user_bp)

    @login_manager.unauthorized_handler
    def unauthorized():
        return jsonify({"message": "Authentication required"}), 401

    if init_admin:
        with app.app_context():
            create_admin()

    return app