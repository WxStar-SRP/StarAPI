from typing import Annotated
from sqlmodel import Session,create_engine,SQLModel
from dotenv import dotenv_values

env = dotenv_values(".env")

# PostgreSQL connection variables
PSQL_HOST = env['POSTGRES_HOST']
PSQL_PORT = env['POSTGRES_PORT']
PSQL_USER = env['POSTGRES_USERNAME']
PSQL_PASS = env['POSTGRES_PASSWORD']
PSQL_DB = env['POSTGRES_DB']

database_url = f"postgresql://{PSQL_USER}:{PSQL_PASS}@{PSQL_HOST}:{PSQL_PORT}/{PSQL_DB}"
engine = create_engine(database_url, echo=True)

def get_session():
    with Session(engine) as session:
        yield session
        
def init_database():
    SQLModel.metadata.create_all(engine)