from flask import Flask

from app.routers.questions import questions_bp
from app.routers.categories import categories_bp  # new
from app.models import db, migrate
from config import DevelopmentConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(questions_bp)
    app.register_blueprint(categories_bp)  # new

    return app