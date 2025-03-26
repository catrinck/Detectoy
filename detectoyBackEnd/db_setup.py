import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Configurações
DB_NAME = "detectoy"
DB_USER = "postgres"  # Altere se necessário
DB_PASSWORD = "12345678"  # Altere para sua senha
DB_HOST = "localhost"
DB_PORT = "5432"

def setup_database():
    try:
        # Conecta ao PostgreSQL
        conn = psycopg2.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        
        # Cria o banco de dados
        cursor.execute(f"DROP DATABASE IF EXISTS {DB_NAME}")
        cursor.execute(f"CREATE DATABASE {DB_NAME}")
        print(f"Banco de dados '{DB_NAME}' criado com sucesso!")
        
        # Cria o usuário do banco
        cursor.execute("DROP ROLE IF EXISTS detectoy")
        cursor.execute("""
            CREATE ROLE detectoy WITH
            LOGIN
            NOSUPERUSER
            NOCREATEDB
            NOCREATEROLE
            INHERIT
            NOREPLICATION
            CONNECTION LIMIT -1
            PASSWORD 'detectoy';
        """)
        
        # Concede privilégios
        cursor.execute(f"GRANT ALL PRIVILEGES ON DATABASE {DB_NAME} TO detectoy")
        print("Usuário 'detectoy' criado e privilégios concedidos!")
        
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    setup_database()