from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, List
from ..services.auth_service import get_password_hash, verify_password
from ..database import get_db
from sqlalchemy.orm import Session
from ..models import User, Manager, Employee
from ..schemas import UserCreate, UserUpdate, UserResponse
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

class UserInput(BaseModel):
    cpf: str
    nome: str
    email: str
    senha: str
    cameras: Optional[bool] = False
    relatorios: Optional[bool] = False

# Gerentes
@router.get("/gerentes", response_model=List[UserResponse])
async def list_managers(db: Session = Depends(get_db)):
    """Lista todos os gerentes"""
    try:
        managers = db.query(Manager).all()
        return managers
    except Exception as e:
        logger.error(f"Erro ao listar gerentes: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao listar gerentes")

@router.post("/gerentes", response_model=UserResponse)
async def create_manager(user: UserCreate, db: Session = Depends(get_db)):
    """Cria um novo gerente"""
    try:
        # Verifica se já existe um usuário com o mesmo CPF ou email
        existing_user = db.query(User).filter(
            (User.cpf == user.cpf) | (User.email == user.email)
        ).first()
        
        if existing_user:
            raise HTTPException(status_code=400, detail="CPF ou email já cadastrado")
        
        # Cria o gerente
        hashed_password = get_password_hash(user.senha)
        db_manager = Manager(
            cpf=user.cpf,
            nome=user.nome,
            email=user.email,
            senha=hashed_password,
            type="manager"  # Define o tipo explicitamente
        )
        db.add(db_manager)
        db.commit()
        db.refresh(db_manager)
        return db_manager
    except Exception as e:
        logger.error(f"Erro ao criar gerente: {str(e)}")
        try:
            db.rollback()
        except:
            pass
        raise HTTPException(status_code=500, detail=f"Erro ao criar gerente: {str(e)}")

@router.get("/gerentes/{cpf}", response_model=UserResponse)
async def get_manager(cpf: str, db: Session = Depends(get_db)):
    """Obtém um gerente específico"""
    try:
        manager = db.query(Manager).filter(Manager.cpf == cpf).first()
        if not manager:
            raise HTTPException(status_code=404, detail="Gerente não encontrado")
        return manager
    except Exception as e:
        logger.error(f"Erro ao obter gerente: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao obter gerente")

@router.put("/gerentes/{cpf}", response_model=UserResponse)
async def update_manager(cpf: str, user: UserUpdate, db: Session = Depends(get_db)):
    """Atualiza um gerente"""
    try:
        db_manager = db.query(Manager).filter(Manager.cpf == cpf).first()
        if not db_manager:
            raise HTTPException(status_code=404, detail="Gerente não encontrado")
        
        # Atualiza os campos
        for field, value in user.dict(exclude_unset=True).items():
            if field == "senha":
                value = get_password_hash(value)
            setattr(db_manager, field, value)
        
        db.commit()
        db.refresh(db_manager)
        return db_manager
    except Exception as e:
        logger.error(f"Erro ao atualizar gerente: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao atualizar gerente")

@router.delete("/gerentes/{cpf}")
async def delete_manager(cpf: str, db: Session = Depends(get_db)):
    """Remove um gerente"""
    try:
        db_manager = db.query(Manager).filter(Manager.cpf == cpf).first()
        if not db_manager:
            raise HTTPException(status_code=404, detail="Gerente não encontrado")
        
        db.delete(db_manager)
        db.commit()
        return {"message": "Gerente removido com sucesso"}
    except Exception as e:
        logger.error(f"Erro ao remover gerente: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao remover gerente")

# Funcionários
@router.get("/funcionarios", response_model=List[UserResponse])
async def list_employees(db: Session = Depends(get_db)):
    """Lista todos os funcionários"""
    try:
        employees = db.query(Employee).all()
        return employees
    except Exception as e:
        logger.error(f"Erro ao listar funcionários: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao listar funcionários")

@router.post("/funcionarios", response_model=UserResponse)
async def create_employee(user: UserCreate, db: Session = Depends(get_db)):
    """Cria um novo funcionário"""
    try:
        # Verifica se já existe um usuário com o mesmo CPF ou email
        existing_user = db.query(User).filter(
            (User.cpf == user.cpf) | (User.email == user.email)
        ).first()
        
        if existing_user:
            raise HTTPException(status_code=400, detail="CPF ou email já cadastrado")
        
        # Cria o funcionário
        hashed_password = get_password_hash(user.senha)
        db_employee = Employee(
            cpf=user.cpf,
            nome=user.nome,
            email=user.email,
            senha=hashed_password,
            cameras=user.cameras,
            relatorios=user.relatorios,
            type="employee"  # Define o tipo explicitamente
        )
        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)
        return db_employee
    except Exception as e:
        logger.error(f"Erro ao criar funcionário: {str(e)}")
        try:
            db.rollback()
        except:
            pass
        raise HTTPException(status_code=500, detail=f"Erro ao criar funcionário: {str(e)}")

@router.get("/funcionarios/{cpf}", response_model=UserResponse)
async def get_employee(cpf: str, db: Session = Depends(get_db)):
    """Obtém um funcionário específico"""
    try:
        employee = db.query(Employee).filter(Employee.cpf == cpf).first()
        if not employee:
            raise HTTPException(status_code=404, detail="Funcionário não encontrado")
        return employee
    except Exception as e:
        logger.error(f"Erro ao obter funcionário: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao obter funcionário")

@router.put("/funcionarios/{cpf}", response_model=UserResponse)
async def update_employee(cpf: str, user: UserUpdate, db: Session = Depends(get_db)):
    """Atualiza um funcionário"""
    try:
        db_employee = db.query(Employee).filter(Employee.cpf == cpf).first()
        if not db_employee:
            raise HTTPException(status_code=404, detail="Funcionário não encontrado")
        
        # Atualiza os campos
        for field, value in user.dict(exclude_unset=True).items():
            if field == "senha":
                value = get_password_hash(value)
            setattr(db_employee, field, value)
        
        db.commit()
        db.refresh(db_employee)
        return db_employee
    except Exception as e:
        logger.error(f"Erro ao atualizar funcionário: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao atualizar funcionário")

@router.delete("/funcionarios/{cpf}")
async def delete_employee(cpf: str, db: Session = Depends(get_db)):
    """Remove um funcionário"""
    try:
        db_employee = db.query(Employee).filter(Employee.cpf == cpf).first()
        if not db_employee:
            raise HTTPException(status_code=404, detail="Funcionário não encontrado")
        
        db.delete(db_employee)
        db.commit()
        return {"message": "Funcionário removido com sucesso"}
    except Exception as e:
        logger.error(f"Erro ao remover funcionário: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao remover funcionário")
