def calculate_bmi(height_m: float, weight_kg: float) -> float:
    if height_m <= 0 or weight_kg <= 0:
        raise ValueError("La taille et le poids doivent être des nombres positifs.")
    bmi = weight_kg / (height_m ** 2)
    return bmi


def calculate_bmr(height_cm: float, weight_kg: float, age_years: int, gender: str) -> float:
    if weight_kg <= 0 or height_cm <= 0 or age_years <= 0:
        raise ValueError("Le poids, la taille et l'âge doivent être des nombres positifs.")
    
    gender = gender.lower()
    if gender not in ["male", "female"]:
        raise ValueError("Le genre doit être 'male' ou 'female'.")
    
    if gender == "male":
        bmr = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age_years)
    else:
        bmr = 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age_years)

    return bmr
