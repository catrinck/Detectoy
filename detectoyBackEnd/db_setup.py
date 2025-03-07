import psycopg

user = "postgres"
password = "12345678"

print("Connecting to database with user=" + user + " and password=" + password)

conn = psycopg.connect("user=" + user + " password=" + password)
conn.autocommit = True

print("Connection succeeded")

with conn:
    with conn.cursor() as curs:
        print("Dropping database 'detectoy' if exists.")

        curs.execute('''DROP DATABASE IF EXISTS detectoy;''')

        print("Database 'detectoy' dropped. Re-creating it.")

        curs.execute('''CREATE DATABASE detectoy
                        WITH
                        OWNER = postgres
                        ENCODING = 'UTF8'
                        TABLESPACE = pg_default
                        CONNECTION LIMIT = -1
                        IS_TEMPLATE = False;
                    '''
                     )
        
        print("Database 'detectoy' created.")
        print("Dropping role 'detectoy' if exists.")

        curs.execute('''DROP ROLE IF EXISTS detectoy;''')

        print("Role 'detectoy' dropped. Re-creating it.")

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
        
        print("Role 'detectoy' created.")
        print("Granting permissions to role.")

        curs.execute('''GRANT TEMPORARY, CONNECT ON DATABASE detectoy TO PUBLIC;
                        GRANT ALL ON DATABASE detectoy TO detectoy;
                        GRANT ALL ON DATABASE detectoy TO postgres;
                        GRANT postgres TO detectoy;
                        ALTER ROLE detectoy SET client_encoding TO 'utf8';
                        ALTER ROLE detectoy SET default_transaction_isolation TO 'READ COMMITTED';
                        ALTER ROLE detectoy SET TimeZone TO 'UTC';
                    '''
                    )
        
        print("Permissions granted.")

        print("Closing connection.")
        
conn.close()

print("Connection closed.")
print("Terminating.")
