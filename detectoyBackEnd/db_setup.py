import psycopg

conn = psycopg.connect("user=postgres password=12345678")
conn.autocommit = True

with conn:
    with conn.cursor() as curs:
        curs.execute('''CREATE DATABASE detectoy
                        WITH
                        OWNER = postgres
                        ENCODING = 'UTF8'
                        LC_COLLATE = 'Portuguese_Brazil.1252'
                        LC_CTYPE = 'Portuguese_Brazil.1252'
                        LOCALE_PROVIDER = 'libc'
                        TABLESPACE = pg_default
                        CONNECTION LIMIT = -1
                        IS_TEMPLATE = False;
                    '''
                     )
        curs.execute('''CREATE ROLE detectoy WITH
                        LOGIN
                        NOSUPERUSER
                        INHERIT
                        NOCREATEDB
                        NOCREATEROLE
                        NOREPLICATION
                        NOBYPASSRLS
                        ENCRYPTED PASSWORD 'SCRAM-SHA-256$4096:jr0AVFrIBxRzm83tfd8GXg==$c0m2+mkiSy7LizjEroS+aD4oSPFVwxYMC9wLiQTpK00=:yN3vNrjXOvyaldTJFRTcfABzTq/8Q441QbPw/jL4NxA=';
                      '''
                     )
        curs.execute('''GRANT TEMPORARY, CONNECT ON DATABASE detectoy TO PUBLIC;
                        GRANT ALL ON DATABASE detectoy TO detectoy;
                        GRANT ALL ON DATABASE detectoy TO postgres;
                        GRANT postgres TO detectoy;
                        ALTER ROLE detectoy SET client_encoding TO 'utf8';
                        ALTER ROLE detectoy SET default_transaction_isolation TO 'READ COMMITTED';
                        ALTER ROLE detectoy SET TimeZone TO 'UTC';
                    '''
                    )

conn.commit()
conn.close()