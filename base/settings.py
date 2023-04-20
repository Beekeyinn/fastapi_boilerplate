import os
from dotenv import load_dotenv
from fastapi_mail import ConnectionConfig


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path=env_path)


class EmailConfig:
    MAIL_USERNAME: str = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD: str = os.getenv("MAIL_PASSWORD")
    MAIL_FROM: str = os.getenv("MAIL_FROM")
    MAIL_PORT: int = os.getenv("MAIL_PORT")
    MAIL_SERVER: str = os.getenv("MAIL_SERVER")
    MAIL_FROM_NAME: str = os.getenv("MAIL_FROM_NAME")


class CorsConfig:
    CORS_ALLOWED_ORIGINS: list = list(os.getenv("CORS_ALLOWED_ORIGINS"))
    CORS_ALLOWED_METHODS: list = list(os.getenv("CORS_ALLOWED_METHODS"))
    CORS_ALLOWED_HEADERS: list = list(os.getenv("CORS_ALLOWED_HEADERS"))
    CORS_ALLOW_CREDENTIALS: bool = bool(os.getenv("CORS_ALLOW_CREDENTIALS"))


class Database:
    PROJECT_NAME: str = "Shopify Google Review Scrapping"
    PROJECT_VERSION: str = "1.0.0"

    DATABASE_USERNAME: str = os.getenv("DATABASE_USERNAME", "postgres")
    DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD", "postgres")
    DATABASE_SERVER: str = os.getenv("DATABASE_SERVER", "127.0.0.1")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "google_scrape")
    DATABASE_PORT: str = os.getenv("DATABASE_PORT", 5432)
    DATABASE_DRIVER: str = os.getenv("DATABASE_DRIVER", "postgresql")

    DATABASE_URL = f"{DATABASE_DRIVER}://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_SERVER}:{DATABASE_PORT}/{DATABASE_NAME}"


database = Database()
email_settings = EmailConfig()

EMAILCONGIFURATION = ConnectionConfig(
    MAIL_USERNAME=email_settings.MAIL_USERNAME,
    MAIL_PASSWORD=email_settings.MAIL_PASSWORD,
    MAIL_FROM=email_settings.MAIL_FROM,
    MAIL_PORT=email_settings.MAIL_PORT,
    MAIL_SERVER=email_settings.MAIL_SERVER,
    MAIL_FROM_NAME=email_settings.MAIL_FROM_NAME,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
    TEMPLATE_FOLDER=os.path.join(BASE_DIR, "templates"),
)

TEMPLATE_DIR = "templates"
STATIC_DIR = "static"
STATIC_ROOT = "/static"
STATIC_NAME = "static"

CHROMEDRIVER = os.getenv("CHROME_DRIVER")
CORS = CorsConfig()

APPS = ["apps.reviews"]
