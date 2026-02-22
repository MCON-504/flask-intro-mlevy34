import requests


base_url = 'http://localhost:5000/'
response = requests.get(f"{base_url}")
print(f"Status Code: {response.status_code}")
print(f"Content: {response.text}")

response = requests.get(f"{base_url}/about")
data = response.json()
for key, value in data.items():
    print(f"{key} : {value}")
name = "Michelle"
response = requests.get(f"{base_url}/greet/{name}")
response = response.json()
if response['name'] == name:
    print("Response contains the correct name")
else:
    print("Response doesn't contain the correct name")



response = requests.get(f"{base_url}/calculate?num1=10&num2=5&operation=add")
response_data = response.json()
if response_data["Status"] == "success":
    print("Verification complete!")
if response_data["Status"] == "error":
    print("Verification incomplete!")


response = requests.get(f"{base_url}/calculate?num1=70&num2=10&operation=multiply")
response_data = response.json()
print(response_data["Result"])


response = requests.get(f"{base_url}/echo")
data = response.json()
if "echoed" in data and True in data.values():
    print("Verification was a success!")
else:
    print("Verification was not a success!")


code = 200
response = requests.get(f"{base_url}/status/{code}")
data = response.text
print(f"Response: {data.text} Status code: {code}")
code = 404
response = requests.get(f"{base_url}/status/{code}")
data = response.text
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


