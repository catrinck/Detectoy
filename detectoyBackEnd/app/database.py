from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Simple database URL
DATABASE_URL = "postgresql://postgres:12345678@localhost:5432/detectoy"

# Create engine
engine = create_engine(DATABASE_URL)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for models
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()