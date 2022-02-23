from typing import List

from pydantic import PostgresDsn, BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    API_STR: str = "/api"
    PROJECT_NAME: str = "licenta backend"

    SECRET_KEY: str = "c7b3ce1fd25e0dd17366611de0149aaa8ea3942660716aadc61510cae7dc3300"
    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # DATABASE_URI: str = "postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/licenta"
    DATABASE_URI: str = "postgresql+psycopg2://ofqkorzsuftujt:0e482520c1959fc7dffbf5e0390f10f512e67ba1c9699c713ea83e45e7b26250@ec2-54-170-212-187.eu-west-1.compute.amazonaws.com:5432/dapoqt4ebioh8o"

    SHOW_DDL = False

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:3000"]


settings = Settings()
