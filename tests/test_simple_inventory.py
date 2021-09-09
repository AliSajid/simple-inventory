from simple_inventory import __version__, create_app
# import pytest
import json

app = create_app()
app.testing = True
client = app.test_client()


def test_version():
    assert __version__ == "0.1.0"


def test_root():
    response = client.get("/")
    data = json.loads(response.data)
    assert data["status_code"] == 200
    assert data["response"] == "Hello"
