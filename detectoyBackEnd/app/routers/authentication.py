from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from ..services.auth_service import verify_password, create_access_token
from ..database import get_db
from sqlalchemy.orm import Session
from ..models import Manager, Employee
from datetime import timedelta
import logging
import traceback

router = APIRouter()
logger = logging.getLogger(__name__)

# Configuração do OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Login(BaseModel):
    email: str  # Pode ser email ou CPF
    senha: str

class Token(BaseModel):
    access_token: str
    token_type: str
    user_type: str
    user_data: dict

@router.post("/login/gerentes/", response_model=Token)
async def login_manager(login: Login, db: Session = Depends(get_db)):
    """Login de gerentes - aceita email ou CPF"""
    try:
        logger.info(f"Tentativa de login para gerente: {login.email}")
        
        # Busca o gerente pelo email ou CPF
        manager = db.query(Manager).filter(
            (Manager.email == login.email) | (Manager.cpf == login.email)
        ).first()
        
        if not manager:
            logger.warning(f"Gerente não encontrado: {login.email}")
            raise HTTPException(status_code=401, detail="Email/CPF ou senha incorretos")
        
        # Verifica a senha
        if not verify_password(login.senha, manager.senha):
            logger.warning(f"Senha incorreta para gerente: {login.email}")
            raise HTTPException(status_code=401, detail="Email/CPF ou senha incorretos")
        
        logger.info(f"Login bem-sucedido para gerente: {login.email}")
        
        # Cria o token de acesso
        access_token = create_access_token(
            data={"sub": manager.email, "type": "manager"},
            expires_delta=timedelta(days=1)
        )
        
        # Prepara os dados do usuário
        user_data = {
            "cpf": manager.cpf,
            "nome": manager.nome,
            "email": manager.email
        }
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user_type": "manager",
            "user_data": user_data
        }
    except HTTPException as e:
        # Repassa a exceção HTTP
        raise e
    except Exception as e:
        stack_trace = traceback.format_exc()
        logger.error(f"Erro no login de gerente: {str(e)}\n{stack_trace}")
        raise HTTPException(status_code=500, detail=f"Erro ao realizar login: {str(e)}")

@router.post("/login/funcionarios/", response_model=Token)
async def login_employee(login: Login, db: Session = Depends(get_db)):
    """Login de funcionários - aceita email ou CPF"""
    try:
        logger.info(f"Tentativa de login para funcionário: {login.email}")
        
        # Busca o funcionário pelo email ou CPF
        employee = db.query(Employee).filter(
            (Employee.email == login.email) | (Employee.cpf == login.email)
        ).first()
        
        if not employee:
            logger.warning(f"Funcionário não encontrado: {login.email}")
            raise HTTPException(status_code=401, detail="Email/CPF ou senha incorretos")
        
        # Verifica a senha
        if not verify_password(login.senha, employee.senha):
            logger.warning(f"Senha incorreta para funcionário: {login.email}")
            raise HTTPException(status_code=401, detail="Email/CPF ou senha incorretos")
        
        logger.info(f"Login bem-sucedido para funcionário: {login.email}")
        
        # Cria o token de acesso
        access_token = create_access_token(
            data={"sub": employee.email, "type": "employee"},
            expires_delta=timedelta(days=1)
        )
        
        # Prepara os dados do usuário
        user_data = {
            "cpf": employee.cpf,
            "nome": employee.nome,
            "email": employee.email,
            "cameras": employee.cameras,
            "relatorios": employee.relatorios
        }
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user_type": "employee",
            "user_data": user_data
        }
    except HTTPException as e:
        # Repassa a exceção HTTP
        raise e
    except Exception as e:
        stack_trace = traceback.format_exc()
        logger.error(f"Erro no login de funcionário: {str(e)}\n{stack_trace}")
        raise HTTPException(status_code=500, detail=f"Erro ao realizar login: {str(e)}")