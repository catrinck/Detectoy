from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    """Classe base para usuários"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    cpf = Column(String, unique=True, index=True)
    nome = Column(String)
    email = Column(String, unique=True, index=True)
    senha = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    type = Column(String)  # Campo para discriminação

    __mapper_args__ = {
        "polymorphic_identity": "user",
        "polymorphic_on": type
    }

class Manager(User):
    """Modelo para gerentes"""
    __tablename__ = "managers"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    __mapper_args__ = {"polymorphic_identity": "manager"}

class Employee(User):
    """Modelo para funcionários"""
    __tablename__ = "employees"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    cameras = Column(Boolean, default=False)
    relatorios = Column(Boolean, default=False)
    __mapper_args__ = {"polymorphic_identity": "employee"}

class Detection(Base):
    """Modelo para detecções"""
    __tablename__ = "detections"

    id = Column(Integer, primary_key=True, index=True)
    defect_type = Column(String)
    confidence = Column(Float)
    image_path = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_email = Column(String, ForeignKey("users.email")) 