from fastapi import APIRouter, HTTPException, BackgroundTasks
from fastapi.responses import StreamingResponse
from ..services.webcam_service import webcam_service
import cv2
import base64
import numpy as np
import time
import asyncio
import logging

router = APIRouter()

# Configuração de logging
logger = logging.getLogger(__name__)

@router.get("/webcam/start")
async def start_webcam():
    """Inicia a captura da webcam"""
    try:
        success = webcam_service.start_camera()
        if success:
            logger.info("Webcam iniciada com sucesso")
            return {"message": "Webcam iniciada com sucesso"}
        logger.info("Webcam já está ativa")
        return {"message": "Webcam já está ativa"}
    except Exception as e:
        logger.error(f"Erro ao iniciar webcam: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/webcam/stop")
async def stop_webcam():
    """Para a captura da webcam"""
    try:
        success = webcam_service.stop_camera()
        if success:
            logger.info("Webcam parada com sucesso")
            return {"message": "Webcam parada com sucesso"}
        logger.info("Webcam já está parada")
        return {"message": "Webcam já está parada"}
    except Exception as e:
        logger.error(f"Erro ao parar webcam: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/webcam/frame")
async def get_frame():
    """Captura um frame da webcam e faz a detecção"""
    try:
        results = webcam_service.process_frame_with_detection()
        return results
    except Exception as e:
        logger.error(f"Erro ao capturar frame: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/webcam/stream")
async def stream_webcam():
    """Streaming da câmera em tempo real"""
    async def generate_frames():
        try:
            while True:
                try:
                    # Captura o frame em formato JPEG
                    frame = webcam_service.get_frame_jpeg()
                    
                    # Gera o frame para streaming
                    yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                    
                    # Aguarda 50ms antes do próximo frame (20 FPS)
                    await asyncio.sleep(0.05)
                    
                except Exception as e:
                    logger.error(f"Erro no streaming: {str(e)}")
                    await asyncio.sleep(1)  # Aguarda um pouco antes de tentar novamente
                    continue
                    
        except Exception as e:
            logger.error(f"Erro fatal no streaming: {str(e)}")
            raise

    return StreamingResponse(
        generate_frames(),
        media_type='multipart/x-mixed-replace; boundary=frame'
    ) 