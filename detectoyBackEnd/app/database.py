from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
import logging
import traceback

# Carrega as variáveis de ambiente
load_dotenv()

# URL do banco de dados
SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@127.0.0.1:8000/detectoy"
)

# Configuração do logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Cria o engine do SQLAlchemy com log de erros
try:
    # Configurações do engine com parâmetros para estabilidade
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        echo=True,  # Habilita log de SQL
        pool_size=5,  # Número de conexões no pool
        max_overflow=10,  # Máximo de conexões extras permitidas
        pool_timeout=30,  # Timeout para obter uma conexão do pool
        pool_recycle=1800,  # Recicla conexões após 30 minutos
        connect_args={
            "connect_timeout": 10,  # Timeout para estabelecer conexão
            "keepalives": 1,  # Habilita keepalives
            "keepalives_idle": 30,  # Tempo ocioso antes de enviar keepalives
            "keepalives_interval": 10,  # Intervalo entre keepalives
            "keepalives_count": 5  # Número de keepalives antes de desistir
        }
    )
    logger.info(f"Conexão com o banco de dados estabelecida: {SQLALCHEMY_DATABASE_URL}")
except Exception as e:
    stack_trace = traceback.format_exc()
    logger.error(f"Erro ao conectar ao banco de dados: {str(e)}\n{stack_trace}")
    raise

# Cria a sessão do SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria a base para os modelos
Base = declarative_base()

def get_db():
    """Função para obter a sessão do banco de dados"""
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        stack_trace = traceback.format_exc()
        logger.error(f"Erro na sessão do banco de dados: {str(e)}\n{stack_trace}")
        db.rollback()
        raise
    finally:
        db.close()
        logger.debug("Sessão do banco de dados fechada")