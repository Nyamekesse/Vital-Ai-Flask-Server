from flask import Blueprint, jsonify


question_and_answering_bp = Blueprint("query", __name__)


@question_and_answering_bp.route("/query-answer", methods=["POST"])
def question_and_answering_fn():
    return jsonify({"result": "hello"})
