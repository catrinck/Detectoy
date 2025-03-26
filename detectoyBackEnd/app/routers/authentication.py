from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class Login(BaseModel):
    email: str
    senha: str

@router.post("/login/gerentes")
async def login_manager(login: Login):
    return {"message": "Manager login", "token": "sample_token"}

@router.post("/login/funcionarios")
async def login_employee(login: Login):
    return {"message": "Employee login", "token": "sample_token"}