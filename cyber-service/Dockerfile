# Dockerfile (Temporaire pour IA, Cyber et Gateway)
FROM python:3.9-slim

# On installe juste un petit serveur web pour que le conteneur ne s'arrête pas
WORKDIR /app
# Installation des libs ML et API
RUN pip install --no-cache-dir fastapi uvicorn scikit-learn pandas joblib numpy

COPY . .

# IMPORTANT : On entraîne le modèle pendant la construction de l'image
# Comme ça, le fichier model.pkl sera prêt quand le conteneur démarrera
RUN python train_model.py

# Lancement du serveur API sur le port 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]