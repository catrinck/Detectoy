from sqlalchemy import create_engine, text
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_database():
    # Connect to default postgres database
    postgres_engine = create_engine("postgresql://postgres:12345678@localhost:5432/postgres")
    db_name = "detectoy"

    with postgres_engine.connect() as conn:
        # Try to create database
        conn.execute(text("commit"))
        
        # Drop if exists
        conn.execute(text(f"DROP DATABASE IF EXISTS {db_name}"))
        conn.execute(text("commit"))
        
        # Create new database
        conn.execute(text(f"CREATE DATABASE {db_name}"))
        logger.info(f"Database {db_name} created successfully")

    # Create tables in new database
    db_engine = create_engine("postgresql://postgres:12345678@localhost:5432/detectoy")
    from app.models import Base
    Base.metadata.create_all(db_engine)
    logger.info("Tables created successfully")

    return True


if __name__ == "__main__":
    setup_database()