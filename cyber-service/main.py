from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import os

# Initialisation
app = FastAPI(title="SafeDrive IDS", version="1.0")

# Chargement du modèle au démarrage
model_path = "model.pkl"
if os.path.exists(model_path):
    clf = joblib.load(model_path)
else:
    # Fallback si le modèle n'est pas encore créé
    clf = None
    print("⚠️ Attention: model.pkl introuvable. Lancez train_model.py")

# Définition du format des données reçues (JSON)
class NetworkLog(BaseModel):
    duration: float
    src_bytes: float
    dst_bytes: float
    count: int
    srv_count: int

@app.get("/")
def read_root():
    return {"status": "Cyber Service Online", "type": "IDS REST API"}

@app.post("/analyze")
def analyze_traffic(log: NetworkLog):
    if not clf:
        return {"error": "Model not loaded"}

    # Préparation des données pour l'IA
    features = [[log.duration, log.src_bytes, log.dst_bytes, log.count, log.srv_count]]
    
    # Prédiction
    prediction = clf.predict(features)[0] # 0 ou 1
    probability = clf.predict_proba(features)[0][1] # Score de confiance

    result = "ATTACK" if prediction == 1 else "SAFE"
    
    return {
        "status": result,
        "confidence": float(probability),
        "details": "DDoS suspecté" if result == "ATTACK" else "Trafic normal"
    }