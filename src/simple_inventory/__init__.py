"""
The simple-inventory module implements a flask application
that can work as a simple inventory app.
"""

__version__ = "0.1.0"


import json
import os
from flask import Flask


def create_app(test_config=None):
    """
    This is a factory method that will create and return our application

    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY="dev",
        PONY={
            "provider": "postgres",
            "username": "simpinv",
            "password": os.environ.get("ENV_POSTGRES_PASSWORD") or "simpinv",
            "host": os.environ.get("ENV_POSTTGRES_HOST") or "127.0.0.1",
            "database": "simpinv",
        },
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route("/")
    def index():
        resp = {"status_code": 200, "response": "Hello"}
        return json.dumps(resp)

    return app
