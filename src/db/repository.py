import sqlalchemy
from src.core.config import DATABASE_URL


class Repository:
    def __init__(self):
        print(DATABASE_URL)
