import subprocess
import socket
import requests
import pytest


@pytest.fixture(scope="module")
def flask_port():
    """Ask OS for a free port."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        addr = s.getsockname()
        port = addr[1]
        return port


@pytest.fixture(scope="module")
def run_app_win(flask_port):
    """Runs the Flask app for live server testing on Windows"""
    server = subprocess.Popen(
        [
            "flask",
            "--app",
            "flaskapp:create_app('flaskapp.config.TestConfig')",
            "run",
            "--port",
            str(flask_port),
        ]
    )
    try:
        yield server
    finally:
        server.terminate()


def test_home_page_running(run_app_win, flask_port):
    """
    GIVEN a running app
    WHEN the homepage is accessed successfully
    THEN the status code will be 200
    """
    # localhost has the IP address 127.0.0.1, which refers
    # back to your own server on your local computer
    url = f"http://localhost:{flask_port}/"
    response = requests.get(url)
    assert response.status_code == 200
    assert b"<title>Login</title>" in response.content


