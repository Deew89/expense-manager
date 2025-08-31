import requests

print("Hello, Python world!")
response = requests.get("https://api.github.com")
print(response.status_code)