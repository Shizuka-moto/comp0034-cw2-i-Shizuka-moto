from pathlib import Path

# Define the project root path
PROJECT_ROOT = Path(__file__).parent


class Config:
    """Base configuration class."""

    SECRET_KEY = "YY3R4fQ5OmlmVKOSlsVHew"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(
        PROJECT_ROOT.joinpath("data", "database.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class ProdConfig(Config):
    """Production configuration class."""

    pass


class DevConfig(Config):
    """Development configuration class."""

    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True


class TestConfig(Config):
    """Testing configuration class."""

    TESTING = True
    SQLALCHEMY_ECHO = False
    WTF_CSRF_ENABLED = False
