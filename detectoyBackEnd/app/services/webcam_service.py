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

    def _initialize_camera(self):
        """Inicializa a câmera se ainda não estiver inicializada"""
        if self.camera is None:
            # Tenta diferentes índices de câmera
            for camera_index in range(2):  # Tenta as primeiras duas câmeras
                self.camera = cv2.VideoCapture(camera_index)
                if self.camera.isOpened():
                    # Configura a resolução da câmera
                    self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                    self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
                    return True
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

webcam_service = WebcamService() 