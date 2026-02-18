import requests


base_url = 'http://localhost:5000/'
response = requests.get(f"{base_url}")
print(f"Status Code: {response.status_code}")
print(f"Content: {response.text}")

response = requests.get(f"{base_url}/about")
data = response.text
for key, value in data.items():
    print(f"{key} : {value}")
name = "Michelle"
response = requests.get(f"{base_url}/greet/{name}")
response = response.json()
if response['name'] == name:
    print("Response contains the correct name")
else:
    print("Response doesn't contain the correct name")


def test_calc_function(response):
    global response
    if requests.args.get('num2') == 0 and requests.args.get('operation') == 'divide':
        print("Division by zero error")
    else:
        response = response.json()
        print(f"Response:{response}")

response = requests.get(f"{base_url}/calculate?num1=10&num2=5&operation=add")
test_calc_function(response)
response = requests.get(f"{base_url}/calculate?num1=70&num2=10&operation=multiply")
test_calc_function(response)


response = requests.get_json(f"{base_url}/echo")
data = response.json()
if "echoed" in data and True in data.values():
    print("Verification was a success!")
else:
    print("Verification was not a success!")


code = 200
response = requests.get(f"{base_url}/status/{code}")
data = response.json()
print(f"Response: {data.text} Status code: {code}")
code = 404
response = requests.get(f"{base_url}/status/{code}")
data = response.json()
print(f"Response: {data.text} Status code: {code}")


response = requests.get('http://localhost:5000/')
custom_header = response.headers.get('X-Custom-Header')
if custom_header == "FlaskRocks":
    print("Correct header!")
else:
    print("incorrect header")
print(f"Custom Header: {custom_header}")

response = requests.get('http://localhost:5000/calculate?num1=10&num2=0&operation=divide')
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")
if response.status_code == 400:
    status = True
else:
    status = False

if "error" in response.json():
    message = True
else:
    message = False
if message and status:
    print("Correct response!")
else:
    print("incorrect response")


