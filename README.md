# 🚍 SafeDrive Monitor: Plateforme de Mobilité Intelligente & Sécurisée

![CI Status](https://github.com/CHYou2Sef/SafeDrive-Platform/actions/workflows/ci-pipeline.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)

## 📖 À propos
**SafeDrive Monitor** est une architecture microservices distribuée dédiée à la **Smart City (Mobilité)**. Elle vise à sécuriser les transports en commun en surveillant l'état du conducteur (IA) et l'intégrité du réseau du véhicule (Cybersécurité).

Ce projet unifié valide les objectifs de 4 modules d'ingénierie : **SOA, IA, Cybersécurité, et DevOps**.

---

## 🏗️ Architecture Technique (SOA)

Le projet respecte une architecture **Microservices** stricte, orchestrée par une API Gateway.
Chaque service a une responsabilité unique et utilise un protocole de communication spécifique :

| Service | Rôle | Protocole | Stack Technique |
| :--- | :--- | :--- | :--- |
| **IA Service** | Analyse faciale du conducteur (Fatigue/Colère) | **gRPC** (Stream) | Python, DeepFace, TensorFlow |
| **Cyber Service** | IDS (Détection d'Intrusion) Réseau | **REST** | Python, FastAPI, Scikit-learn |
| **Driver API** | Gestion administrative des chauffeurs | **GraphQL** | Node.js, Apollo Server |
| **Legacy API** | Données Météo (Simulation système externe) | **SOAP** | Python, Spyne |
| **Gateway** | Point d'entrée unique et routage | **HTTP** | Python, FastAPI |

---

## 🧠 Intelligence Artificielle (IA - Projet 4)
**Module :** Reconnaissance Faciale des Émotions (FER).
* **Modèle :** Utilisation de réseaux de neurones convolutionnels (CNN) pour détecter 7 émotions clés + la fatigue (yeux fermés).
* **XAI (Explicabilité) :** Intégration de Grad-CAM pour visualiser les zones du visage ayant déclenché la décision (ex: yeux pour la fatigue).

## 🛡️ Cybersécurité (Projet 1)
**Module :** IDS Intelligent (Intrusion Detection System).
* **Approche :** Machine Learning Supervisé (Random Forest / XGBoost).
* **Dataset :** Entraîné sur le dataset **NSL-KDD** pour classifier le trafic en "Normal" ou "Attaque" (DoS, Probe).
* **Isolation :** Le service tourne dans un conteneur isolé pour éviter la propagation en cas de compromission.

## 🚀 DevOps & Automatisation
Le projet suit les pratiques **DevSecOps** modernes :
* **CI/CD :** Pipeline GitHub Actions (Build & Test automatisés à chaque push).
* **Conteneurisation :** Images Docker optimisées (Alpine/Slim).
* **Orchestration :** Déploiement via **Docker Compose** (Local) et manifests **Kubernetes** (Prod).
* **Monitoring :** Architecture prête pour Prometheus/Grafana.

---

## 🛠️ Installation et Démarrage

### Pré-requis
* Docker & Docker Compose
* Git

### Lancement rapide
```bash
# 1. Cloner le projet
git clone https://github.com/CHYou2Sef/SafeDrive-Platform.git (https://github.com/CHYou2Sef/SafeDrive-Platform.git)
cd SafeDrive-Platform

# 2. Lancer l'infrastructure complète
docker-compose up --build

#Accès aux Services

Dashboard Unifié (Frontend) : http://localhost:3000

API Gateway (Swagger) : http://localhost:8000/docs

IA Service (gRPC) : http://localhost:5001

Cyber Service (REST) : http://localhost:5002