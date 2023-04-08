from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./new.db"

SQLALCHEMY_DATABASE_URL = "postgresql://tulwvjtz:9L0FfLBakCl3NVhwhef86o4JJCTWWopl@babar.db.elephantsql.com/tulwvjtz"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

        
