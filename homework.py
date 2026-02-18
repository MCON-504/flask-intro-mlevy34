from flask import Flask, request

app = Flask(__name__)

@app.before_request
def before_request():
    print(f"request received: {request.method} {request.path}")
@app.after_request
def after_request(response):
    response["custom header"] = "FlaskRocks"
    return response
@app.teardown_request
def teardown_request(exception):
    print("Exception during request: {exception}")
