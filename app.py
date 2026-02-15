from flask import Flask, request, current_app

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/")
def route1():
    return  " <h1>Welcome to My Flask API!</h1>"

@app.route("/about")
def route2():
    return  {"name": "Your Name", "course": "MCON-504 - Backend Development", "semester": "Spring 2025"}

@app.route("/greet/<name>")
def route3(name):
    return  f"Hello,{name} ! Welcome to Flask."
@app.route("/calculate")
def calculate():
    operation = request.args.get('operation')
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')

    if operation is None or num1 is None or num2 is None:
        return "Missing parameter"
    num1 = float(num1)
    num2 = float(num2)
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1 / num2

    return {"Result" : result, "Operation" : operation}
@app.route("/echo", methods = ["POST"])
def route5():
    response = request.get_json()
    response["Echoed"] = True
    return response
@app.route("/status/<int:code>")
def route6(code):
    message = f"This is a {code} error"
    return message, code
if __name__ == '__main__':
    app.run(debug=True)