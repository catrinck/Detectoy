import os
import sys
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from urllib.parse import urlparse
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_database():
    load_dotenv()
    
    # Obtém a URL do banco de dados do arquivo .env
    db_url = os.getenv('DATABASE_URL')
    if not db_url:
        logger.error("DATABASE_URL não encontrada nas variáveis de ambiente")
        sys.exit(1)
    
    try:
        # Parse da URL para extrair as informações
        parsed_url = urlparse(db_url)
        db_name = parsed_url.path[1:]  # Remove a barra inicial
        
        logger.info(f"Tentando conectar ao PostgreSQL na porta {parsed_url.port}")
        
        # Cria uma URL para conectar ao PostgreSQL sem especificar o banco de dados
        postgres_url = f"postgresql://{parsed_url.username}:{parsed_url.password}@{parsed_url.hostname}:{parsed_url.port}/postgres"
        logger.info(f"URL de conexão: {postgres_url}")
        
        # Conecta ao PostgreSQL
        engine = create_engine(postgres_url)
        
        with engine.connect() as conn:
            logger.info("Conexão estabelecida com sucesso!")
            
            # Desconecta outros usuários do banco de dados
            conn.execute(text(f"""
                SELECT pg_terminate_backend(pg_stat_activity.pid)
                FROM pg_stat_activity
                WHERE pg_stat_activity.datname = '{db_name}'
                AND pid <> pg_backend_pid()
            """))
            conn.execute(text("COMMIT"))
            
            # Verifica se o banco de dados existe
            result = conn.execute(text(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}'"))
            exists = result.scalar() is not None
            
            if exists:
                # Dropa o banco de dados existente para recriar do zero
                logger.info(f"Banco de dados '{db_name}' já existe. Recriando...")
                conn.execute(text("COMMIT"))
                conn.execute(text(f"DROP DATABASE IF EXISTS {db_name}"))
                conn.execute(text("COMMIT"))
                conn.execute(text(f"CREATE DATABASE {db_name}"))
                logger.info(f"Banco de dados '{db_name}' recriado com sucesso!")
            else:
                # Cria o banco de dados
                conn.execute(text("COMMIT"))
                conn.execute(text(f"CREATE DATABASE {db_name}"))
                logger.info(f"Banco de dados '{db_name}' criado com sucesso!")
        
        # Conecta ao banco de dados criado e cria as tabelas
        db_engine = create_engine(db_url)
        
        # Importa e cria todas as tabelas
        from app.models import Base, User, Manager, Employee, Detection
        Base.metadata.create_all(bind=db_engine)
        logger.info("Tabelas criadas com sucesso!")
        
        logger.info("Configuração do banco de dados concluída com sucesso!")
            
    except Exception as e:
        logger.error(f"Erro ao configurar o banco de dados: {str(e)}")
        logger.error("Verifique se o PostgreSQL está rodando na porta 8000")
        logger.error("Execute: netstat -ano | findstr :8000 para verificar a porta")
        sys.exit(1)

if __name__ == "__main__":
    setup_database()