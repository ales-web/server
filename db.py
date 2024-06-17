from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

db_url = "postgresql://postgres:postgres@localhost:5432/postgres"

engine = create_engine(db_url)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
