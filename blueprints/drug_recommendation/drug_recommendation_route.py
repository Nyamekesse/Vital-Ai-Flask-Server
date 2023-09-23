from flask import Blueprint, jsonify, request
import numpy as np
import joblib
from errors import handle_not_processable_error

drug_recommendation_bp = Blueprint("recommend", __name__)

disease_list = [
    "Acne",
    "Allergy",
    "Diabetes",
    "Fungal infection",
    "Urinary tract infection",
    "Malaria",
    "Migraine",
    "Hepatitis B",
    "AIDS",
]

disease_dict = {
    "Acne": 0,
    "Allergy": 1,
    "Diabetes": 2,
    "Fungal infection": 3,
    "Urinary tract infection": 4,
    "Malaria": 5,
    "Migraine": 6,
    "Hepatitis B": 7,
    "AIDS": 8,
}

vital_ai_drug_recommendation_model = joblib.load(
    "ml_models/vital_ai_drug_recommendation_model.pkl"
)


@drug_recommendation_bp.route("/recommend-drug", methods=["POST"])
def recommend_drug_fn():
    data = request.get_json()
    if not data:
        return handle_not_processable_error("")
    if not data["disease"] or not data["sex"] or not data["age"]:
        return handle_not_processable_error("")
    patient_disease = data["disease"]
    sex = 1 if data["sex"].lower() == "male" else 0
    age = int(data["age"])

    if patient_disease in disease_list:
        mapped_disease = disease_dict.get(patient_disease)

        test = [mapped_disease, sex, age]
        test = np.array(test)
        test = np.array(test).reshape(1, -1)

        prediction = vital_ai_drug_recommendation_model.predict(test)
        prediction = prediction[0]

        return jsonify({"result": prediction})
    return handle_not_processable_error("Specified disease not found in database")
