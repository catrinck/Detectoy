from fastapi import APIRouter, HTTPException
from ..services.webcam_service import webcam_service
import cv2
import base64
import numpy as np

router = APIRouter()

@router.get("/webcam/start")
async def start_webcam():
    """Inicia a captura da webcam"""
    try:
        success = webcam_service.start_camera()
        if success:
            return {"message": "Webcam iniciada com sucesso"}
        return {"message": "Webcam já está ativa"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/webcam/stop")
async def stop_webcam():
    """Para a captura da webcam"""
    try:
        success = webcam_service.stop_camera()
        if success:
            return {"message": "Webcam parada com sucesso"}
        return {"message": "Webcam já está parada"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/webcam/frame")
async def get_frame():
    """Captura um frame da webcam e faz a detecção"""
    try:
        results = webcam_service.get_frame()
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 