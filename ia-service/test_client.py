import grpc
import numpy as np
import cv2
import ia_service_pb2
import ia_service_pb2_grpc

def run():
    # 1. Connexion au serveur (localhost:50051)
    # Note: Si on lance ce script DEPUIS le conteneur, on utilise 'localhost'
    channel = grpc.insecure_channel('localhost:50051')
    stub = ia_service_pb2_grpc.DriverMonitorStub(channel)

    print("🤖 Envoi d'une image vide pour tester...")

    # 2. Création d'une fausse image (Noir, 480x640)
    # C'est juste pour voir si le serveur répond, pas pour tester la fatigue
    dummy_image = np.zeros((480, 640, 3), dtype=np.uint8)
    _, encoded_img = cv2.imencode('.jpg', dummy_image)
    
    # 3. Appel gRPC
    response = stub.AnalyzeDriver(
        ia_service_pb2.ImageRequest(image_data=encoded_img.tobytes())
    )

    # 4. Résultat
    print(f"✅ Réponse du serveur :")
    print(f"   - Status: {response.status}")
    print(f"   - Emotion: {response.emotion}")
    print(f"   - Confiance: {response.confidence}")

if __name__ == '__main__':
    run()