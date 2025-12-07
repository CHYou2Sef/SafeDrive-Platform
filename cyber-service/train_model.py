import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

# 1. Génération de fausses données réseaux (Simulation NSL-KDD)
# Features: [duration, src_bytes, dst_bytes, count, srv_count]
print("🧠 Entraînement du modèle IDS (Simulation)...")

# Données normales (petits paquets, durée courte)
X_normal = np.random.rand(500, 5) * 100 
y_normal = np.zeros(500) # 0 = Safe

# Données d'attaques (gros paquets, durée longue - ex: DoS)
X_attack = np.random.rand(500, 5) * 1000 + 500
y_attack = np.ones(500) # 1 = Attack

X = np.concatenate((X_normal, X_attack))
y = np.concatenate((y_normal, y_attack))

# 2. Entraînement du Random Forest
clf = RandomForestClassifier(n_estimators=10)
clf.fit(X, y)

# 3. Sauvegarde du modèle
joblib.dump(clf, "model.pkl")
print("✅ Modèle 'model.pkl' sauvegardé avec succès !")