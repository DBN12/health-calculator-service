# Health Calculator API

Ce projet contient une application Flask permettant de calculer deux indicateurs de santé importants : 

- **BMI (Body Mass Index)** : L'indice de masse corporelle, utile pour évaluer si une personne est en surpoids, sous-poids, ou dans une plage normale.
- **BMR (Basal Metabolic Rate)** : Le métabolisme de base, qui correspond à la quantité de calories brûlées par le corps au repos.

## Structure du projet

- **`app.py`** : Fichier principal contenant l'application Flask et les deux endpoints `/bmi` et `/bmr`.
- **`health_utils.py`** : Contient les fonctions pour effectuer les calculs du BMI et du BMR.
- **`requirements.txt`** : Liste des bibliothèques nécessaires pour faire fonctionner l'application.
- **`Makefile`** : Fichier d'automatisation pour faciliter les tâches (voir la section "Utilisation" ci-dessous).
- **`Dockerfile`** : Permet de créer une image Docker pour déployer l'application.
- **`test.py`** : Contient des tests pour valider le fonctionnement du calcul et des endpoints.
- **`.github/workflows/ci-cd.yml`** : Configuration pour le pipeline CI/CD GitHub Actions, permettant de déployer l'application automatiquement sur Azure Web App.

## Fonctionnalités

- **Calcul du BMI :** Utilisez le point de terminaison `/bmi` avec un payload JSON contenant `height_m` (taille en mètres) et `weight_kg` (poids en kg).
- **Calcul du BMR :** Utilisez le point de terminaison `/bmr` avec un payload JSON contenant `height_cm` (taille en cm), `weight_kg` (poids en kg), `age_years` (âge en années), et `gender` (genre, `"male"` ou `"female"`).

---


