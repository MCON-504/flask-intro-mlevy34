from flask import Flask, request, jsonify, current_app

app = Flask(__name__)


@app.route("/")
def route1():
    return  " <h1>Welcome to My Flask API!</h1>"

@app.route("/about")
def route2():
    return  {"name": "Your Name", "course": "MCON-504 - Backend Development", "semester": "Spring 2025"}

@app.route("/greet/<name>")
def route3(name):
    return  f"'<h1>Hello, %s!</h1>' % name"
@app.route("/calculate")
def calculate():
    operation = request.args.get('operation')
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')

    if operation is None or num1 is None or num2 is None:
        return "Missing parameter"
    num1 = float(num1)
    num2 = float(num2)
    try:
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            result = num1 / num2
        else:
            return "Invalid operation"
        return {"Result" : result, "Operation" : operation}
    except Exception as e:
    # Log the exception and return an error response
        print(f"Error occurred: {e}")
        return {"error": "An error occurred during calculation"}


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

@app.route('/debug/routes')
def show_routes():
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append({
            'endpoint': rule.endpoint,
            'methods': list(rule.methods),
            'path': str(rule)
        })
    return jsonify(routes)