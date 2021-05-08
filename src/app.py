from flask import Flask

from src.blueprints.api import api_bp
from src.blueprints.health import health_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.settings")

    app.register_blueprint(api_bp)
    app.register_blueprint(health_bp)

    return app
