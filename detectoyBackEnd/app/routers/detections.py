from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from ..services.yolo_service import yolo_service

router = APIRouter(prefix="/detections", tags=["detections"])

@router.get("/")
async def get_detections():
    """Get API status and available endpoints"""
    return {
        "status": "active",
        "endpoints": {
            "POST /": "Upload an image for detection",
            "GET /": "Get API status"
        }
    }

@router.post("/")
async def detect_objects(file: UploadFile = File(...)):
    """Upload an image and detect broken screens or cases"""
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    try:
        contents = await file.read()
        results = yolo_service.process_image(contents)
        return JSONResponse(content=results)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))