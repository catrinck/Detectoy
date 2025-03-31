import cv2
import numpy as np
from datetime import datetime
import uuid
import os
from pathlib import Path
from ..services.yolo_service import yolo_service

class WebcamService:
    def __init__(self):
        self.camera = None
        self.is_running = False
        self.output_dir = Path("app/static/results")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.last_save_time = 0
        self.save_interval = 2
        self.frame_count = 0
        self.detection_interval = 3  # Processa detecção a cada 3 frames

    def _initialize_camera(self):
        """Inicializa a câmera se ainda não estiver inicializada"""
        if self.camera is None:
            camera_indices = [1, 0]
            
            for camera_index in camera_indices:
                print(f"Tentando câmera com índice {camera_index}")
                self.camera = cv2.VideoCapture(camera_index)
                
                if self.camera.isOpened():
                    ret, frame = self.camera.read()
                    if ret:
                        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
                        print(f"Câmera {camera_index} inicializada com sucesso")
                        return True
                    else:
                        print(f"Câmera {camera_index} não consegue capturar frames")
                        self.camera.release()
                        self.camera = None
                else:
                    print(f"Câmera {camera_index} não disponível")
                    self.camera.release()
                    self.camera = None
            
            raise Exception("Nenhuma câmera disponível encontrada")
        return True

    def start_camera(self):
        """Inicia a captura da câmera"""
        try:
            if not self.is_running:
                self._initialize_camera()
                self.is_running = True
                self.frame_count = 0
                return True
            return False
        except Exception as e:
            if self.camera:
                self.camera.release()
                self.camera = None
            self.is_running = False
            raise Exception(f"Erro ao iniciar câmera: {str(e)}")

    def stop_camera(self):
        """Para a captura da câmera"""
        try:
            if self.camera is not None:
                self.is_running = False
                self.camera.release()
                self.camera = None
                return True
            return False
        except Exception as e:
            raise Exception(f"Erro ao parar câmera: {str(e)}")

    def get_frame(self):
        """Captura um frame e faz a detecção"""
        try:
            # Garante que a câmera está inicializada
            if not self.is_running:
                self.start_camera()

            if self.camera is None:
                raise Exception("Câmera não está ativa")

            ret, frame = self.camera.read()
            if not ret:
                raise Exception("Não foi possível capturar o frame")

            # Converte o frame para bytes
            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()

            # Faz a detecção usando o serviço YOLO
            results = yolo_service.process_image(frame_bytes)
            return results
        except Exception as e:
            raise Exception(f"Erro ao capturar frame: {str(e)}")

    def get_frame_jpeg(self):
        """Captura um frame e retorna em formato JPEG"""
        try:
            if not self.is_running:
                self.start_camera()

            if self.camera is None:
                raise Exception("Câmera não está ativa")

            ret, frame = self.camera.read()
            if not ret:
                raise Exception("Não foi possível capturar o frame")

            # Converte o frame para JPEG
            _, buffer = cv2.imencode('.jpg', frame)
            return buffer.tobytes()
        except Exception as e:
            raise Exception(f"Erro ao capturar frame: {str(e)}")

    def process_frame_with_detection(self):
        """Processa um frame com detecção e salva se encontrar defeitos"""
        try:
            if not self.is_running:
                self.start_camera()

            if self.camera is None:
                raise Exception("Câmera não está ativa")

            ret, frame = self.camera.read()
            if not ret:
                raise Exception("Não foi possível capturar o frame")

            self.frame_count += 1
            
            # Faz detecção apenas a cada N frames para otimizar performance
            if self.frame_count % self.detection_interval == 0:
                # Converte o frame para bytes
                _, buffer = cv2.imencode('.jpg', frame)
                frame_bytes = buffer.tobytes()

                # Faz a detecção usando o serviço YOLO
                results = yolo_service.process_image(frame_bytes)
                
                # Verifica se detectou algum defeito
                if results.get("broken_screen") or results.get("broken_shell"):
                    current_time = datetime.now().timestamp()
                    if current_time - self.last_save_time >= self.save_interval:
                        self.last_save_time = current_time
                        print(f"Defeito detectado: {'Tela Quebrada' if results['broken_screen'] else ''} {'Carcaça Quebrada' if results['broken_shell'] else ''}")
                
                return results
            
            # Se não é frame de detecção, retorna resultado vazio
            return {
                "broken_screen": False,
                "broken_shell": False,
                "confidence_scores": [],
                "detected_classes": [],
                "result_image": None
            }
            
        except Exception as e:
            raise Exception(f"Erro ao processar frame: {str(e)}")

webcam_service = WebcamService() 