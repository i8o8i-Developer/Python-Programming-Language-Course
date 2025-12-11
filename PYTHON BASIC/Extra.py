# Requests Module
"""
The Requests Module Is A Popular Python Library For Making HTTP Requests.
It Simplifies Sending HTTP/1.1 Requests And Handling Responses.
It's Not Part Of The Standard Library, So It Needs To Be Installed.

Installation:
pip install requests

How It Works:
- requests.get(url) - GET Request
- requests.post(url, data=data) - POST Request
- requests.put(url, data=data) - PUT Request
- requests.delete(url) - DELETE Request
- Response Object Has status_code, text, json(), headers, Etc.
"""

# First, Install Requests If Not Already Installed
# Run: pip install requests

import requests

# Basic GET Request
print("--- Basic GET Request ---")
response = requests.get("https://httpbin.org/get")
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text[:200]}...")  # First 200 Chars

# GET With Parameters
print("\n--- GET With Parameters ---")
params = {"key": "value", "foo": "bar"}
response = requests.get("https://httpbin.org/get", params=params)
print(f"URL: {response.url}")
print(f"Status: {response.status_code}")

# POST Request
print("\n--- POST Request ---")
data = {"username": "anubhav", "password": "secret"}
response = requests.post("https://httpbin.org/post", data=data)
print(f"Status: {response.status_code}")
print(f"Response JSON: {response.json()}")

# POST with JSON
print("\n--- POST with JSON ---")
json_data = {"name": "Anubhav", "age": 21, "city": "Delhi"}
response = requests.post("https://httpbin.org/post", json=json_data)
print(f"Status: {response.status_code}")
print(f"Sent JSON: {json_data}")
print(f"Response: {response.json()['json']}")  # Echoed back

# Headers
print("\n--- Custom Headers ---")
headers = {"User-Agent": "My Python App", "Authorization": "Bearer Token123"}
response = requests.get("https://httpbin.org/headers", headers=headers)
print(f"Status: {response.status_code}")
print(f"Headers Sent: {response.json()['headers']}")

# Handling Errors
print("\n--- Error Handling ---")
try:
    response = requests.get("https://httpbin.org/status/404", timeout=5)
    response.Raise_For_Status()  # Raises Exception For Bad Status
except requests.exceptions.RequestException as e:
    print(f"Request Failed: {e}")

# Timeouts
print("\n--- Timeouts ---")
try:
    response = requests.get("https://httpbin.org/delay/1", timeout=2)  # 2 Second Timeout
    print(f"Success: {response.status_code}")
except requests.exceptions.Timeout:
    print("Request Timed Out")

# Sessions (For Cookies, Auth)
print("\n--- Sessions ---")
with requests.Session() as session:
    session.auth = ("user", "pass")  # Basic Auth
    session.headers.update({"User-Agent": "MyApp/1.0"})
    response = session.get("https://httpbin.org/basic-auth/user/pass")
    print(f"Auth Status: {response.status_code}")

# File Upload
print("\n--- File Upload ---")
files = {"file": open("Text.txt", "rb")}
response = requests.post("https://httpbin.org/post", files=files)
print(f"File Upload Status: {response.status_code}")
files["file"].close()

# Downloading Files
print("\n--- Downloading Files ---")
response = requests.get("https://httpbin.org/image/png")
with open("Downloaded_Image.png", "wb") as f:
    f.write(response.content)
print("Image Downloaded As 'Downloaded_Image.png'")

# JSON Response
print("\n--- JSON Response Handling ---")
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if response.status_code == 200:
    data = response.json()
    print(f"Post ID: {data['id']}")
    print(f"Title: {data['title']}")

# Proxies
print("\n--- Proxies (Example) ---")
# proxies = {"http": "http://proxy.com:8080", "https": "https://proxy.com:8080"}
# response = requests.get("https://httpbin.org/ip", proxies=proxies)
# print(f"IP via proxy: {response.json()}")

print("\nRequests Module Makes HTTP Communication Simple And Powerful!")
# Original Code Below (Keeping For Reference)
def Fahrenheit_To_Celsius():
    try:
        F = float(input("Enter The Temperature In Fahrenheit: "))
        C = f"The Value Of Temperature In Celsius : {((F-32)*5)/9}"
        return C
    except ValueError:
        return "Invalid Input! Please Enter A Number."

print(Fahrenheit_To_Celsius())


# Progress Bar Using Flush
import time as Time
def ProgressBar(Number):
    print(' [ ' , end='')
    for Out in range(Number):
        Time.sleep(0.1)
        print('#' , end='' , flush=True)
    print(' ] ' , end='')

print(ProgressBar(50))

class Programmer:
    Language = "Hindi"
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age 
    def PrintInfo(self):
        return f"Name : {self.Name} , Age : {self.Age} , Your Language : {self.Language}"

P = Programmer("Anubhav", 21)
print(P.PrintInfo())

def Fahrenheit_To_Celsius():
    try:
        F = float(input("Enter The Temperature In Fahrenheit: "))
        C = f"The Value Of Temperature In Celsius : {((F-32)*5)/9}"
        return C
    except ValueError:
        return "Invalid Input! Please Enter A Number."

print(Fahrenheit_To_Celsius())


# Progress Bar Using Flush
import time as Time
def ProgressBar(Number):
    print(' [ ' , end='')
    for Out in range(Number):
        Time.sleep(0.1)
        print('#' , end='' , flush=True)
    print(' ] ' , end='')

print(ProgressBar(50))

class Programmer:
    Language = "Hindi"
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age 
    def PrintInfo(self):
        return f"Name : {self.Name} , Age : {self.Age} , Your Language : {self.Language}"

P = Programmer("Anubhav", 21)
print(P.PrintInfo())