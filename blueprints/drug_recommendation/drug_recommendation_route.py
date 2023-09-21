from flask import Blueprint, jsonify


drug_recommendation_bp = Blueprint("recommend", __name__)


@drug_recommendation_bp.route("/recommend-drug", methods=["POST"])
def recommend_drug_fn():
    return jsonify({"result": "hello"})
