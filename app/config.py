from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pathlib import Path
import environ
import os
from datetime import timedelta
BASE_DIR = Path(__file__).resolve().parent
env_file=os.path.join(BASE_DIR,".env")
env=environ.Env()
env.read_env(env_file)
DB_NAME=env('DB_NAME')
DB_PORT=env('DB_PORT')
DB_HOST=env('DB_HOST')
DB_USER=env('DB_USER')
DB_PASSWORD=env('DB_PASSWORD')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine= create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind= engine)
Base = declarative_base()