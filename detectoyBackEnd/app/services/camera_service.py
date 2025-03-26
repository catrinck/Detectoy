import cv2
import base64
import numpy as np
from .yolo_service import yolo_service
import logging
import os
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CameraService:
    def __init__(self):
        self.camera = None
        self._retry_count = 0
        self._max_retries = 3
        self.save_dir = "app/static/detections"
        os.makedirs(self.save_dir, exist_ok=True)
    
    def start_camera(self, camera_id=0):
        while self._retry_count < self._max_retries:
            try:
                if self.camera is None:
                    self.camera = cv2.VideoCapture(camera_id)
                    self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                    self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
                    if not self.camera.isOpened():
                        raise RuntimeError(f"Could not access camera {camera_id}")
                    logger.info(f"Camera {camera_id} started successfully")
                    self._retry_count = 0
                    return True
            except Exception as e:
                self._retry_count += 1
                logger.error(f"Failed to start camera: {str(e)}")
                if self.camera:
                    self.camera.release()
                    self.camera = None
        
        raise RuntimeError("Failed to start camera after multiple attempts")
    
    def get_frame(self):
        if not self.camera:
            self.start_camera()
            
        ret, frame = self.camera.read()
        if not ret:
            raise RuntimeError("Failed to capture frame")
            
        return frame
    
    def process_frame(self, frame):
        try:
            # Processar com YOLO
            success, encoded_img = cv2.imencode('.jpg', frame)
            if not success:
                raise RuntimeError("Failed to encode image")
            
            img_bytes = encoded_img.tobytes()
            results = yolo_service.process_image(img_bytes)
            
            # Se detectou algo, salvar a imagem
            if results["broken_screen"] or results["broken_shell"]:
                timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
                filename = f"detection_{timestamp}.jpg"
                save_path = os.path.join(self.save_dir, filename)
                
                # Desenhar as detecções na imagem
                annotated_frame = frame.copy()
                if results["broken_screen"]:
                    cv2.putText(annotated_frame, "Tela Quebrada", (10, 30),
                              cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                if results["broken_shell"]:
                    cv2.putText(annotated_frame, "Carcaça Quebrada", (10, 60),
                              cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                
                cv2.imwrite(save_path, annotated_frame)
                results["saved_image"] = f"/static/detections/{filename}"
            
            # Converter frame para base64 para envio
            _, buffer = cv2.imencode('.jpg', frame)
            img_base64 = base64.b64encode(buffer).decode('utf-8')
            
            return {
                "frame": img_base64,
                "status": "success",
                **results
            }
            
        except Exception as e:
            logger.error(f"Error processing frame: {str(e)}")
            return {
                "status": "error",
                "error": str(e)
            }
    
    def stop_camera(self):
        if self.camera:
            self.camera.release()
            self.camera = None
            logger.info("Camera stopped")

camera_service = CameraService()