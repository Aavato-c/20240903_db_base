import os
import sys
import dotenv
import logging
from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base



logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.info("Database connection established")

dotenv.load_dotenv()

try:
    SQL_DB_NAME = os.getenv("SQLITE_DB_NAME")
    if not SQL_DB_NAME:
        dotenv.load_dotenv(".env.example")
        SQL_DB_NAME = os.getenv("SQLITE_DB_NAME")
        if not SQL_DB_NAME:
            raise Exception("SQLITE_DB_NAME not set in .env or .env.example")
    SQLALCHEMY_DATABASE_URL = f"sqlite:///./{SQL_DB_NAME}.sqlite3"
except Exception as e:
    log.error(f"Error loading environment variables: {e}")
    sys.exit(1)


# Create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}) 

# Create a session object that will be used to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

# Create the database tables
Base.metadata.create_all(bind=engine)

@contextmanager
def get_db() -> Generator[Session, None, None]:
    """
    Get database connection object that can be used to interact with the database.
    It is a generator function that will automatically close the connection after the operation is done.
    The connection object is used to interact with the database in crud.py.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
