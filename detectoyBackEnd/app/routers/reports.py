from fastapi import APIRouter

router = APIRouter()

@router.get("/relatorio")
async def get_report():
    return {"message": "Generate report"}

@router.get("/erro")
async def list_errors():
    return {"message": "List errors"}