from dotenv import load_dotenv
import os 
from envparse import Env

env = Env()
load_dotenv()

class ConfigDatabase:
    DB_HOST = os.environ.get("DB_HOST")
    DB_PORT = os.environ.get("DB_PORT")
    DB_NAME = os.environ.get("DB_NAME")
    DB_PASS = os.environ.get("DB_PASS")
    DB_USER = os.environ.get("DB_USER")
    DATABASE_URL = env.str(
        "DATABASE_URL", 
        default = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

