# Dockerfile (Temporaire pour IA, Cyber et Gateway)
FROM python:3.9-slim

# On installe juste un petit serveur web pour que le conteneur ne s'arrête pas
WORKDIR /app
RUN echo "Service en cours d'execution..." > index.html

# On lance un serveur HTTP basique
CMD ["python", "-m", "http.server", "80"]
