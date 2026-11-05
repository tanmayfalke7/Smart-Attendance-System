from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Smart Office Attendance System"
    APP_ENV: str = "development"
    DEBUG: bool = True
    APP_TIMEZONE: str = "Asia/Kolkata"

    DB_HOST: str = "127.0.0.1"
    DB_PORT: int = 3306
    DB_NAME: str = "attendance_db"
    DB_USER: str = "attendance_app"
    DB_PASSWORD: str

    DB_POOL_SIZE: int = 5
    DB_MAX_OVERFLOW: int = 10

    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )

    @property
    def DATABASE_URL(self) -> str:
        from sqlalchemy.engine import URL

        return URL.create(
            drivername="mysql+pymysql",
            username=self.DB_USER,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            port=self.DB_PORT,
            database=self.DB_NAME,
            query={"charset": "utf8mb4"}
        ).render_as_string(hide_password=False)


settings = Settings()