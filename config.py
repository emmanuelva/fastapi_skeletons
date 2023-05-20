from pydantic import BaseSettings


class Settings(BaseSettings):
    db_connection_string: str = ''

    class Config:
        env_file = '.env'


settings = Settings()
