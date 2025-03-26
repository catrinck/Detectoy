import cv2
from app.services.webcam_service import webcam_service

def test_webcam():
    try:
        # Inicia a câmera
        webcam_service.start_camera()
        print("Câmera iniciada com sucesso")
        
        # Captura um frame
        frame = webcam_service.get_frame()
        print("Frame capturado com sucesso")
        
        # Processa o frame
        results = webcam_service.process_frame(frame)
        print("Frame processado com sucesso")
        print("Resultados:", results)
        
        # Para a câmera
        webcam_service.stop_camera()
        print("Câmera parada com sucesso")
        
    except Exception as e:
        print(f"Erro: {str(e)}")
        webcam_service.stop_camera()

if __name__ == "__main__":
    test_webcam() 