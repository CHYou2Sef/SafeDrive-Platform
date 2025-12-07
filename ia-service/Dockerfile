# Dockerfile (Temporaire pour IA, Cyber et Gateway)
FROM python:3.9-slim

# On installe juste un petit serveur web pour que le conteneur ne s'arrête pas
WORKDIR /app

# RUN echo "Service en cours d'execution..." > index.html

# On lance un serveur HTTP basique
# CMD ["python", "-m", "http.server", "80"]

# Installation des dépendances système pour OpenCV (nécessaire pour l'image)
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0

# Installation des librairies Python
# grpcio-tools sert à compiler le fichier .proto
RUN pip install grpcio grpcio-tools deepface tf-keras opencv-python-headless numpy

# Copie du code
COPY . .

# Génération automatique du code gRPC au démarrage (Astuce gain de temps)
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ia_service.proto

# Lancement du serveur
CMD ["python", "server.py"]

#test 
