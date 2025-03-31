from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from ..services.webcam_service import webcam_service
import asyncio
import json
from typing import List, Dict
import logging

router = APIRouter()

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.connection_count = 0

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        self.connection_count += 1
        logger.info(f"Nova conexão estabelecida. Total: {self.connection_count}")

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
            self.connection_count -= 1
            logger.info(f"Conexão removida. Total: {self.connection_count}")

    async def broadcast(self, message: Dict):
        disconnected = []
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except Exception as e:
                logger.error(f"Erro ao enviar mensagem: {str(e)}")
                disconnected.append(connection)
        
        # Remove conexões que falharam
        for connection in disconnected:
            self.disconnect(connection)

manager = ConnectionManager()

@router.websocket("/ws/detections")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            try:
                # Processa o frame com detecção
                results = webcam_service.process_frame_with_detection()
                
                # Envia os resultados para todos os clientes conectados
                await manager.broadcast(results)
                
                # Aguarda 500ms antes da próxima captura
                await asyncio.sleep(0.5)
                
            except Exception as e:
                logger.error(f"Erro durante o processamento: {str(e)}")
                await asyncio.sleep(1)  # Aguarda um pouco antes de tentar novamente
            
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        logger.info("Cliente desconectado")
    except Exception as e:
        manager.disconnect(websocket)
        logger.error(f"Erro no WebSocket: {str(e)}") 