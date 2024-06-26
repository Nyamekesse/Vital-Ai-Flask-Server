from flask import Flask
from config import DevConfig, ProConfig, TestConfig
from exts import db
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

from blueprints.disease_prediction.disease_prediction_routes import (
    disease_prediction_bp,
)
from blueprints.drug_recommendation.drug_recommendation_route import (
    drug_recommendation_bp,
)


def create_app():
    app = Flask(__name__)
    if app.config.get("ENV") == "production":
        app.config.from_object(ProConfig)
    elif app.config.get("ENV") == "testing":
        app.config.from_object(TestConfig)
    else:
        app.config.from_object(DevConfig)

    with app.app_context():
        CORS(app)
        Bcrypt(app)
        JWTManager(app)
        db.init_app(app)
        app.register_blueprint(drug_recommendation_bp, url_prefix="/api")
        app.register_blueprint(disease_prediction_bp, url_prefix="/api")

        @app.route("/api/ping", methods=["GET"])
        def ping():
            return "Server is active!"

    return app
