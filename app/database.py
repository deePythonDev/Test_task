import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from pathlib import Pat
import logging
import environ
import os
BASE_DIR = Path(__file__).resolve().parent
env_file=os.path.join(BASE_DIR,".env")
env=environ.Env()
env.read_env(env_file)
DB_NAME=env('DB_NAME')
DB_PORT=env('DB_PORT')
DB_HOST=env('DB_HOST')
DB_USER=env('DB_USER')
DB_PASSWORD=env('DB_PASSWORD')


def create_database_model():
     
    try:
        logging.critical("DB doesn't exist creating db...")
        conn = psycopg2.connect(dbname='postgres',
                user=f"{DB_USER}", host=f'{DB_HOST}',
                password=f"{DB_PASSWORD}")
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        cur = conn.cursor()
        cur.execute(sql.SQL("CREATE DATABASE {}").format(
                    sql.Identifier(f"{DB_NAME}"))
                    )
        
        cur.close()
        conn.close()
    except Exception as e:
        print(e)
            
            
