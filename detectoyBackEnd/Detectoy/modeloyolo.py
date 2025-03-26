from fastapi import FastAPI, UploadFile, File, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import cv2
import numpy as np
import os
import uuid
from datetime import datetime
from ultralytics import YOLO
import asyncio

app = FastAPI()

# Configurações
CONFIG = {
    'CONFIDENCE_THRESHOLD': 0.35,
    'MODEL_PATH': os.path.join("models", "thebest.pt"),
    'OUTPUT_DIR': "results",
    'SAVE_INTERVAL_MS': 10,
    'TARGET_CLASSES': ['tela_quebrada', 'carcaca_quebrada']
}

model = YOLO(CONFIG['MODEL_PATH'])

class ConnectionManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    async def broadcast(self, data: dict):
        for connection in self.active_connections:
            await connection.send_json(data)

manager = ConnectionManager()

@app.post("/detect/")
async def detect_objects(file: UploadFile = File(...)):
    image_data = await file.read()
    image = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)
    
    results = model(image)[0]
    detected_classes = [model.names[int(box.cls)] for box in results.boxes]
    
    if any(cls in CONFIG['TARGET_CLASSES'] for cls in detected_classes):
        filename = f"{datetime.now().strftime('%Y%m%d-%H%M%S')}-{uuid.uuid4().hex}.jpg"
        output_path = os.path.join(CONFIG['OUTPUT_DIR'], filename)
        cv2.imwrite(output_path, results.plot())
        
        await manager.broadcast({
            "type": "detection",
            "data": {
                "broken_screen": "tela_quebrada" in detected_classes,
                "broken_shell": "carcaca_quebrada" in detected_classes,
                "image_url": f"/results/{filename}"
            }
        })
    
    return {
        "broken_screen": "tela_quebrada" in detected_classes,
        "broken_shell": "carcaca_quebrada" in detected_classes
    }

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    while True:
        await websocket.receive_text() 

app.mount("/results", StaticFiles(directory="results"), name="results")
app.mount("/", StaticFiles(directory="static"), name="static")