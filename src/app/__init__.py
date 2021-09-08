__version__ = '0.1.0'


from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def index():
    response =  {"response": "Hello", "status_code": 200}
    return json.dumps(response)
