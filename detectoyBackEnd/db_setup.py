import psycopg

try:
    # Conecta ao banco de dados padrão para criar o novo banco
    conn = psycopg.connect("host=localhost user=postgres password=12345678 dbname=postgres")
    conn.autocommit = True

    with conn.cursor() as curs:
        # Verifica se o banco de dados já existe
        curs.execute("SELECT 1 FROM pg_database WHERE datname = 'detectoy';")
        if curs.fetchone():
            print("O banco de dados 'detectoy' já existe.")
        else:
            # Cria o banco de dados detectoy
            print("Criando o banco de dados 'detectoy'...")
            curs.execute('''
                CREATE DATABASE detectoy
                WITH
                OWNER = postgres
                ENCODING = 'UTF8'
                LC_COLLATE = 'Portuguese_Brazil.1252'
                LC_CTYPE = 'Portuguese_Brazil.1252'
                LOCALE_PROVIDER = 'libc'
                TABLESPACE = pg_default
                CONNECTION LIMIT = -1
                IS_TEMPLATE = False;
            ''')
            print("Banco de dados 'detectoy' criado com sucesso.")

        # Verifica se o role já existe
        curs.execute("SELECT 1 FROM pg_roles WHERE rolname = 'detectoy';")
        if curs.fetchone():
            print("O role 'detectoy' já existe.")
        else:
            # Cria o role detectoy com as permissões
            print("Criando o role 'detectoy'...")
            curs.execute('''
                CREATE ROLE detectoy WITH
                LOGIN
                NOSUPERUSER
                INHERIT
                NOCREATEDB
                NOCREATEROLE
                NOREPLICATION
                NOBYPASSRLS
                ENCRYPTED PASSWORD 'SCRAM-SHA-256$4096:jr0AVFrIBxRzm83tfd8GXg==$c0m2+mkiSy7LizjEroS+aD4oSPFVwxYMC9wLiQTpK00=:yN3vNrjXOvyaldTJFRTcfABzTq/8Q441QbPw/jL4NxA=';
            ''')
            print("Role 'detectoy' criado com sucesso.")

        # Configura as permissões no banco de dados detectoy
        print("Configurando permissões no banco de dados 'detectoy'...")
        curs.execute('''
            GRANT TEMPORARY, CONNECT ON DATABASE detectoy TO PUBLIC;
            GRANT ALL ON DATABASE detectoy TO detectoy;
            GRANT ALL ON DATABASE detectoy TO postgres;
            GRANT postgres TO detectoy;
            ALTER ROLE detectoy SET client_encoding TO 'utf8';
            ALTER ROLE detectoy SET default_transaction_isolation TO 'READ COMMITTED';
            ALTER ROLE detectoy SET TimeZone TO 'UTC';
        ''')
        print("Permissões configuradas com sucesso.")

except psycopg.OperationalError as e:
    print(f"Erro de conexão: {e}")
except Exception as e:
    print(f"Erro durante a execução: {e}")
finally:
    if 'conn' in locals() and not conn.closed:
        conn.close()
        print("Conexão encerrada.")
