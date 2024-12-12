from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/bmi', methods=['POST'])
def bmi_endpoint():
    data = request.get_json()
    if not data or "height_m" not in data or "weight_kg" not in data:
        return jsonify({"error": "Données manquantes ou format incorrect."}), 400

    height_m = data["height_m"]
    weight_kg = data["weight_kg"]

    try:
        bmi_value = calculate_bmi(height_m, weight_kg)
        return jsonify({"bmi": round(bmi_value, 2)})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route('/bmr', methods=['POST'])
def bmr_endpoint():
    data = request.get_json()
    required_fields = ["height_cm", "weight_kg", "age_years", "gender"]

    # Vérification de la présence de toutes les clés
    if not data or any(field not in data for field in required_fields):
        return jsonify({"error": "Données manquantes ou format incorrect."}), 400

    height_cm = data["height_cm"]
    weight_kg = data["weight_kg"]
    age_years = data["age_years"]
    gender = data["gender"]

    try:
        bmr_value = calculate_bmr(height_cm, weight_kg, age_years, gender)
        return jsonify({"bmr": round(bmr_value, 2)})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    # Lancement de l'application en local sur le port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
