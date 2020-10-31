from os import environ
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    # Flask variables
    FLASK_ENV = environ.get("FLASK_ENV", "production")
    FLASK_DEBUG = environ.get("FLASK_DEBUG", False)

    # Application variables
    APP_NAME = environ.get("APP_NAME", "Feedma Drive")
    APP_VERSION = environ.get("APP_VERSION", "0.0.1")

