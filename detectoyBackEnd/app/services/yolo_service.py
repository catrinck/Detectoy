from ultralytics import YOLO
import cv2
import os
import numpy as np
from datetime import datetime
import uuid
from pathlib import Path

class YOLOService:
    def __init__(self):
        self.config = {
            'CONFIDENCE_THRESHOLD': 0.35,
            'MODEL_PATH': os.path.join("models", "thebest.pt"),
            'OUTPUT_DIR': "app/static/results",
            'TARGET_CLASSES': ['tela_quebrada', 'carcaca_quebrada']
        }
        self.model = YOLO(self.config['MODEL_PATH'])

    def process_image(self, image_bytes):
        # Converte bytes para numpy array
        nparr = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # Executa a inferência
        results = self.model(image)[0]
        detected_classes = [self.model.names[int(box.cls)] for box in results.boxes]
        
        # Processa os resultados
        broken_screen = "tela_quebrada" in detected_classes
        broken_shell = "carcaca_quebrada" in detected_classes
        
        # Se detectou algum dos defeitos, salva a imagem
        if broken_screen or broken_shell:
            # Cria o diretório de resultados se não existir
            output_dir = Path(self.config['OUTPUT_DIR'])
            output_dir.mkdir(parents=True, exist_ok=True)
            
            # Gera nome único para o arquivo
            filename = f"{datetime.now().strftime('%Y%m%d-%H%M%S')}-{uuid.uuid4().hex}.jpg"
            output_path = output_dir / filename
            
            # Salva a imagem com as detecções
            cv2.imwrite(str(output_path), results.plot())
            
            return {
                "broken_screen": broken_screen,
                "broken_shell": broken_shell,
                "confidence_scores": [float(box.conf) for box in results.boxes],
                "detected_classes": detected_classes,
                "result_image": f"/static/results/{filename}"
            }
        
        # Se não detectou nada, retorna sem salvar a imagem
        return {
            "broken_screen": False,
            "broken_shell": False,
            "confidence_scores": [],
            "detected_classes": [],
            "result_image": None
        }

yolo_service = YOLOService()