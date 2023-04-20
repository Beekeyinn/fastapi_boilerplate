from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from base.settings import database


SQLALCHEMY_DATABASE_URL = database.DATABASE_URL
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # isolation_level="READ UNCOMMITTED",
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
