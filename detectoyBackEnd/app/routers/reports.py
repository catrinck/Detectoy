from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Detection
from datetime import datetime, timedelta
import pandas as pd
import json
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/relatorio")
async def generate_report(
    start_date: str = None,
    end_date: str = None,
    defect_type: str = None,
    db: Session = Depends(get_db)
):
    """Gera um relatório de detecções"""
    try:
        # Converte as datas para objetos datetime
        if start_date:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
        if end_date:
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Query base
        query = db.query(Detection)
        
        # Aplica filtros
        if start_date:
            query = query.filter(Detection.created_at >= start_date)
        if end_date:
            query = query.filter(Detection.created_at <= end_date)
        if defect_type:
            query = query.filter(Detection.defect_type == defect_type)
        
        # Executa a query
        detections = query.all()
        
        # Prepara os dados para o relatório
        report_data = []
        for detection in detections:
            report_data.append({
                "id": detection.id,
                "defect_type": detection.defect_type,
                "confidence": detection.confidence,
                "image_path": detection.image_path,
                "created_at": detection.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "user_email": detection.user_email
            })
        
        # Cria um DataFrame para análise
        df = pd.DataFrame(report_data)
        
        # Gera estatísticas
        stats = {
            "total_detections": len(detections),
            "defects_by_type": df["defect_type"].value_counts().to_dict(),
            "average_confidence": df["confidence"].mean(),
            "detections_by_date": df.groupby(df["created_at"].str[:10]).size().to_dict()
        }
        
        return {
            "data": report_data,
            "statistics": stats
        }
    except Exception as e:
        logger.error(f"Erro ao gerar relatório: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao gerar relatório")

@router.get("/erro")
async def list_errors(
    start_date: str = None,
    end_date: str = None,
    db: Session = Depends(get_db)
):
    """Lista erros de detecção"""
    try:
        # Converte as datas para objetos datetime
        if start_date:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
        if end_date:
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Query base
        query = db.query(Detection).filter(Detection.confidence < 0.5)
        
        # Aplica filtros de data
        if start_date:
            query = query.filter(Detection.created_at >= start_date)
        if end_date:
            query = query.filter(Detection.created_at <= end_date)
        
        # Executa a query
        errors = query.all()
        
        # Prepara os dados
        error_data = []
        for error in errors:
            error_data.append({
                "id": error.id,
                "defect_type": error.defect_type,
                "confidence": error.confidence,
                "image_path": error.image_path,
                "created_at": error.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "user_email": error.user_email
            })
        
        return {
            "total_errors": len(errors),
            "errors": error_data
        }
    except Exception as e:
        logger.error(f"Erro ao listar erros: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao listar erros")