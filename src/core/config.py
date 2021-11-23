from starlette.config import Config


config = Config(".env")

DATABASE_URL = config("EE_DATABASE_URL", cast=str, default="")
DATABASE_NAME = config("EE_DATABASE_NAME", cast=str, default="")


