import requests

request_payload = {

      "name": "chethan",
      "location": "AJP",
      "phone": "789211"

}

response = requests.post("http://localhost:3000/students",json=request_payload)

print(response.status_code)
response_json = response.json()

id = response_json['id']
print(id)
print(response_json)
assert response.status_code == 201
