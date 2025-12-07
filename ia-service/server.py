import sys

# On force l'affichage immédiat
def log(msg):
    print(f"[DEBUG] {msg}", flush=True)

log("Démarrage du script...")


import grpc
from concurrent import futures
import time
import cv2
import numpy as np
log("Importation de Mediapipe en cours...")
import mediapipe as mp
log("Mediapipe importé.")

log("Importation de DeepFace en cours (Peut être long)...")
from deepface import DeepFace
log("DeepFace importé.")

import ia_service_pb2
import ia_service_pb2_grpc

# --- 1. Initialisation de la détection de visage (Mediapipe est + léger que dlib) ---
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Fonction mathématique pour calculer l'ouverture des yeux (EAR)
def calculate_ear(landmarks, eye_indices):
    # Logique similaire au repo GitHub mais adaptée à Mediapipe
    # (Calcul des distances euclidiennes verticales et horizontales)
    # Pour simplifier ici : on regarde la distance verticale entre les paupières
    top = landmarks[eye_indices[12]] # Point haut paupière
    bottom = landmarks[eye_indices[4]] # Point bas paupière
    dist = abs(top.y - bottom.y)
    return dist

class DriverMonitorServicer(ia_service_pb2_grpc.DriverMonitorServicer):
    def AnalyzeDriver(self, request, context):
        print("📸 Analyse image en cours...")
        
        # 1. Conversion des bytes gRPC en image OpenCV
        nparr = np.frombuffer(request.image_data, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        status = "SAFE"
        emotion = "Neutral"
        confidence = 0.0

        # 2. Détection Fatigue (Approche du repo Git adaptée)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0].landmark
            
            # Indices des yeux pour Mediapipe (différents de dlib 68 points)
            left_eye_dist = calculate_ear(landmarks, [33, 160, 158, 133, 153, 144, ...]) # Simplifié
            
            # Seuil empirique (à ajuster)
            if left_eye_dist < 0.02: 
                status = "DANGER"
                emotion = "Fatigue (Eyes Closed)"
                confidence = 0.99
            else:
                # 3. Si les yeux sont ouverts, on vérifie l'émotion (Colère ?)
                # On utilise DeepFace (plus lent mais précis pour l'émotion)
                try:
                    # analyze renvoie une liste d'objets
                    objs = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                    #emotion = objs[0]['dominant_emotion']
                    emotion = "Simulation (DeepFace Disabled)"
                    if emotion in ['angry', 'fear']:
                        status = "DANGER"
                except:
                    pass

        return ia_service_pb2.AnalysisReply(
            status=status,
            emotion=emotion,
            confidence=0.95
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ia_service_pb2_grpc.add_DriverMonitorServicer_to_server(DriverMonitorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("🚀 Serveur IA (Drowsiness + Emotion) démarré...")
    try:
        while True: time.sleep(86400)
    except KeyboardInterrupt: server.stop(0)

if __name__ == '__main__':
    serve()