import logging
from ultralytics import YOLO
import cv2
import os
import numpy as np
from datetime import datetime
import uuid
from pathlib import Path
from dotenv import load_dotenv

# Configuração do logger
logger = logging.getLogger(__name__)

# Carrega variáveis de ambiente
load_dotenv()

class YOLOService:
    def __init__(self):
        self.model = None
        self.model_path = os.getenv('MODEL_PATH', 'models/thebest.pt')
        self.target_classes = ['tela_quebrada', 'carcaca_quebrada']
        self.model_initialized = False
        try:
            self._initialize_model()
        except FileNotFoundError as e:
            logger.warning(f"Modelo não encontrado: {str(e)}. Serviço funcionará sem detecção.")
        except Exception as e:
            logger.warning(f"Erro ao inicializar modelo: {str(e)}. Serviço funcionará sem detecção.")

    def _initialize_model(self):
        """Inicializa o modelo YOLO com verificações de erro"""
        try:
            # Verifica se o arquivo do modelo existe
            if not os.path.exists(self.model_path):
                error_msg = f"Modelo não encontrado em: {self.model_path}"
                logger.error(error_msg)
                raise FileNotFoundError(error_msg)

            # Tenta carregar o modelo com configurações específicas
            self.model = YOLO(self.model_path, task='detect')
            
            # Verifica se as classes alvo estão presentes no modelo
            model_classes = self.model.names
            missing_classes = [cls for cls in self.target_classes if cls not in model_classes.values()]
            if missing_classes:
                error_msg = f"Classes alvo não encontradas no modelo: {missing_classes}"
                logger.error(error_msg)
                raise ValueError(error_msg)

            logger.info("Modelo YOLO inicializado com sucesso")
            self.model_initialized = True
            
        except Exception as e:
            logger.error(f"Erro ao inicializar o modelo YOLO: {str(e)}")
            raise

    def process_image(self, image_data):
        """Processa uma imagem usando o modelo YOLO"""
        try:
            # Se o modelo não está inicializado, retorna detecções vazias
            if not self.model_initialized:
                logger.warning("Processamento de imagem ignorado: modelo não inicializado")
                return []

            # Decodifica a imagem
            nparr = np.frombuffer(image_data, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            if img is None:
                raise ValueError("Não foi possível decodificar a imagem")

            # Verifica se o modelo foi inicializado
            if self.model is None:
                try:
                    self._initialize_model()
                except Exception as e:
                    logger.error(f"Falha ao reinicializar modelo: {str(e)}")
                    return []

            # Realiza a detecção com configurações específicas
            results = self.model(img, conf=0.35, iou=0.45)
            
            # Processa os resultados
            detections = []
            for result in results:
                boxes = result.boxes
                for box in boxes:
                    class_id = int(box.cls[0])
                    confidence = float(box.conf[0])
                    class_name = result.names[class_id]
                    
                    if class_name in self.target_classes:
                        x1, y1, x2, y2 = box.xyxy[0].tolist()
                        detections.append({
                            'class': class_name,
                            'confidence': confidence,
                            'bbox': [x1, y1, x2, y2]
                        })

            # Salva a imagem com as detecções se houver defeitos
            if detections:
                os.makedirs('app/static/results', exist_ok=True)
                save_path = os.path.join('app', 'static', 'results', f'detection_{datetime.now().strftime("%Y%m%d%H%M%S")}.jpg')
                cv2.imwrite(save_path, img)
                logger.info(f"Imagem salva em: {save_path}")

            return detections

        except Exception as e:
            logger.error(f"Erro ao processar imagem: {str(e)}")
            return []

yolo_service = YOLOService()