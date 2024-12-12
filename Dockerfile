FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier tous les fichiers du répertoire actuel vers /app dans le conteneur
COPY . /app

# Installer les dépendances Python
RUN pip install -r requirements.txt

# Exposer le port sur lequel Flask écoute
EXPOSE 5000

# Commande pour lancer l'application au démarrage du conteneur
CMD ["python", "app.py"]
