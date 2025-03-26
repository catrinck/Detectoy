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
            'OUTPUT_DIR': "results",
            'TARGET_CLASSES': ['tela_quebrada', 'carcaca_quebrada']
        }
        self.model = YOLO(self.config['MODEL_PATH'])

    def process_image(self, image_bytes):
        # Convert bytes to numpy array
        nparr = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # Run inference
        results = self.model(image)[0]
        detected_classes = [self.model.names[int(box.cls)] for box in results.boxes]
        
        # Save result image
        filename = f"{datetime.now().strftime('%Y%m%d-%H%M%S')}-{uuid.uuid4().hex}.jpg"
        output_path = os.path.join(self.config['OUTPUT_DIR'], filename)
        
        # Ensure output directory exists
        os.makedirs(self.config['OUTPUT_DIR'], exist_ok=True)
        
        # Save annotated image
        cv2.imwrite(output_path, results.plot())
        
        return {
            "broken_screen": "tela_quebrada" in detected_classes,
            "broken_shell": "carcaca_quebrada" in detected_classes,
            "confidence_scores": [float(box.conf) for box in results.boxes],
            "detected_classes": detected_classes,
            "result_image": f"/static/results/{filename}"
        }

yolo_service = YOLOService()