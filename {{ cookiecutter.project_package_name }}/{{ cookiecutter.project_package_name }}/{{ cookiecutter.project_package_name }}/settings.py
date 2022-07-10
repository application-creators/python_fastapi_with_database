from functools import lru_cache
from typing import List, Optional

from pydantic import BaseSettings

SETTINGS_FILE_PATH = "settings.env"


ROOT_ROUTE = "/"
IDENTIFIER_ROUTE = "/{identifier}"


class Settings(BaseSettings):
    project_name: str

    default_limit: int = 10
    default_offset: int = 0

    cors_enabled: Optional[bool] = False
    cors_allow_origins: Optional[List[str]]
    cors_allow_methods: Optional[List[str]]
    cors_allow_headers: Optional[List[str]]

    database_host: str
    database_port: str
    database_driver: str
    database_user: str
    database_password: str
    database_name: str

    @property
    def database_uri(self):
        return (
            f"{self.database_driver}"
            f"://{self.database_user}:{self.database_password}"
            f"@{self.database_host}:{self.database_port}"
            f"/{self.database_name}"
        )

    class Config:
        env_file = SETTINGS_FILE_PATH


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
