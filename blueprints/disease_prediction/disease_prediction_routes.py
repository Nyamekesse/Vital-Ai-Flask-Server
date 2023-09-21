from flask import Blueprint, jsonify


disease_prediction_bp = Blueprint("predict", __name__)


@disease_prediction_bp.route("/predict-disease", methods=["POST"])
def disease_prediction_fn():
    return jsonify({"result": "hello"})
