import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import inspect
from src.core.config import DATABASE_URL


class Repository:
    __instance = None

    def __init__(self, engine=None, url=None):
        if engine:
            self.engine = engine
        elif url:
            self.engine = create_engine(DATABASE_URL)

        self.connection = self.engine.connect()

    def __del__(self):
        self.connection.close()

    def get_column(self, table_name):
        rows = self.connection.execute(f"SELECT * FROM {table_name}")
        return rows

    def execute(self, query):
        try:
            return self.connection.execute(query)
        except Exception as e:
            # TODO messagebox by error code
            print(e)

    @classmethod
    def create_repository(cls, engine=None, url=None):
        if cls.__instance is None:
            if engine is None and url is None:
                engine = create_engine(DATABASE_URL)
            return Repository(engine=engine)
        else:
            return cls.__instance
