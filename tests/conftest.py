import pytest
from flaskapp import create_app, db
from flaskapp.config import TestConfig

@pytest.fixture(scope="session")
def app():
    """Create a Flask app configured for testing"""
    app = create_app(TestConfig)
    yield app


# Used for Flask route tests
@pytest.fixture(scope="function")
def test_client(app):
    """Create a Flask test client"""
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client