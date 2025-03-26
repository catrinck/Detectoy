import cv2
import base64
import numpy as np
from datetime import datetime
import os
import logging
from .yolo_service import yolo_service

class CameraService:
    def __init__(self):
        self.camera = None
        self.save_dir = "app/static/detections"
        os.makedirs(self.save_dir, exist_ok=True)
        
    def start_camera(self, camera_id=0):
        if self.camera is None:
            self.camera = cv2.VideoCapture(camera_id)
            if not self.camera.isOpened():
                raise RuntimeError("Could not access camera")
            
    def get_frame(self):
        if not self.camera:
            self.start_camera()
            
        ret, frame = self.camera.read()
        if not ret:
            raise RuntimeError("Failed to capture frame")
            
        return frame
    
    def process_frame(self, frame):
        # Convert frame to bytes for YOLO
        success, encoded_img = cv2.imencode('.jpg', frame)
        if not success:
            raise RuntimeError("Failed to encode frame")
            
        img_bytes = encoded_img.tobytes()
        results = yolo_service.process_image(img_bytes)
        
        # Save frame if detection found
        if results.get("broken_screen") or results.get("broken_shell"):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"detection_{timestamp}.jpg"
            save_path = os.path.join(self.save_dir, filename)
            
            # Draw detections
            annotated_frame = frame.copy()
            if results.get("broken_screen"):
                cv2.putText(annotated_frame, "Tela Quebrada", (10, 30),
                          cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            if results.get("broken_shell"):
                cv2.putText(annotated_frame, "Carcaça Quebrada", (10, 60),
                          cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                          
            cv2.imwrite(save_path, annotated_frame)
            results["saved_image"] = f"/static/detections/{filename}"
        
        # Convert frame to base64 for sending
        _, buffer = cv2.imencode('.jpg', frame)
        img_base64 = base64.b64encode(buffer).decode('utf-8')
        
        return {
            "frame": img_base64,
            "status": "success",
            **results
        }
        
    def stop_camera(self):
        if self.camera:
            self.camera.release()
            self.camera = None

camera_service = CameraService()