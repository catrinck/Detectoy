from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class User(BaseModel):
    cpf: str
    nome: str
    email: str
    senha: str
    cameras: Optional[bool] = False
    relatorios: Optional[bool] = False

# Gerentes
@router.get("/gerentes")
async def list_managers():
    return {"message": "List managers"}

@router.post("/gerentes")
async def create_manager(user: User):
    return {"message": "Create manager", "user": user}

@router.get("/gerentes/{cpf}")
async def get_manager(cpf: str):
    return {"message": "Get manager", "cpf": cpf}

@router.put("/gerentes/{cpf}")
async def update_manager(cpf: str, user: User):
    return {"message": "Update manager", "cpf": cpf, "user": user}

@router.delete("/gerentes/{cpf}")
async def delete_manager(cpf: str):
    return {"message": "Delete manager", "cpf": cpf}

# Funcionários
@router.get("/funcionarios")
async def list_employees():
    return {"message": "List employees"}

@router.post("/funcionarios")
async def create_employee(user: User):
    return {"message": "Create employee", "user": user}

@router.get("/funcionarios/{cpf}")
async def get_employee(cpf: str):
    return {"message": "Get employee", "cpf": cpf}

@router.put("/funcionarios/{cpf}")
async def update_employee(cpf: str, user: User):
    return {"message": "Update employee", "cpf": cpf, "user": user}

@router.delete("/funcionarios/{cpf}")
async def delete_employee(cpf: str):
    return {"message": "Delete employee", "cpf": cpf}
