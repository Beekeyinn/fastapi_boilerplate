from typing import Generator
import modulefinder
from .session import engine, SessionLocal
from .base_class import Base
# from .review import *
import importlib


from base.settings import APPS

for app in APPS:
    importlib.import_module(f"{app}.models")



def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
