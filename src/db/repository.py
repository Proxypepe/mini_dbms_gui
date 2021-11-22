import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import inspect
from src.core.config import DATABASE_URL


class Repository:
    def __init__(self):
        self.engine = create_engine(DATABASE_URL)

    def get_column(self, table_name):
        with self.engine.connect() as con:
            rows = con.execute(f"SELECT * FROM {table_name}")
        return rows

