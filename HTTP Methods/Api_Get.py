import requests

response = requests.get("http://localhost:3000/students/2")

print(response.status_code)
print(response.json())

assert response.status_code == 200