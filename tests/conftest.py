# Import the required modules
import pytest
from flaskapp import create_app, db
from flaskapp.config import TestConfig


# Define a pytest fixture for creating a Flask app configured for testing
@pytest.fixture(scope="session")
def app():
    """Create a Flask app configured for testing."""
    app = create_app(TestConfig)
    yield app


# Define a pytest fixture for creating a Flask test client
@pytest.fixture(scope="function")
def test_client(app):
    """Create a Flask test client."""
    # Create a test client for the Flask app
    with app.test_client() as testing_client:
        # Push the app context to be used during testing
        with app.app_context():
            yield testing_client