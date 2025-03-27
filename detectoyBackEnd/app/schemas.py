from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    cpf: str
    nome: str
    email: EmailStr

class UserCreate(UserBase):
    senha: str
    cameras: Optional[bool] = False
    relatorios: Optional[bool] = False

class UserUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    senha: Optional[str] = None
    cameras: Optional[bool] = None
    relatorios: Optional[bool] = None

class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    cameras: Optional[bool] = None
    relatorios: Optional[bool] = None

    class Config:
        from_attributes = True

class DetectionBase(BaseModel):
    defect_type: str
    confidence: float
    image_path: str
    user_email: str

class DetectionCreate(DetectionBase):
    pass

class DetectionResponse(DetectionBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True 