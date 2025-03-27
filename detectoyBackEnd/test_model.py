import os
from app.services.yolo_service import yolo_service
import cv2
import numpy as np

def test_model():
    try:
        # Verifica se o arquivo do modelo existe
        model_path = os.getenv('MODEL_PATH', 'models/thebest.pt')
        if not os.path.exists(model_path):
            print(f"ERRO: O arquivo do modelo não foi encontrado em {model_path}")
            print("Por favor, certifique-se de que o arquivo do modelo está presente no diretório models/")
            return

        # Cria uma imagem de teste (um quadrado branco em fundo preto)
        test_image = np.zeros((640, 480, 3), dtype=np.uint8)
        cv2.rectangle(test_image, (100, 100), (300, 300), (255, 255, 255), -1)

        # Converte a imagem para bytes
        _, buffer = cv2.imencode('.jpg', test_image)
        image_bytes = buffer.tobytes()

        # Processa a imagem
        print("Processando imagem de teste...")
        results = yolo_service.process_image(image_bytes)
        
        print("\nResultados:")
        print(f"Total de detecções: {len(results)}")
        for detection in results:
            print(f"Classe: {detection['class']}")
            print(f"Confiança: {detection['confidence']:.2f}")
            print(f"Bounding Box: {detection['bbox']}")
            print("---")

    except Exception as e:
        print(f"ERRO: {str(e)}")

if __name__ == "__main__":
    test_model() 