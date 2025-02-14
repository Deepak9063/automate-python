import requests
import json

def test_create_new_user():
    update_payload = {
          "name": "manoj",
          "location": "AJP",
          "phone": "789211"
    }

    response = requests.put("http://localhost:3000/students/fd55",json=update_payload)

    print(response.status_code)
    response_json = response.json()
    print(response_json)
    student_id = response_json['id']
    print(student_id)
    assert response.status_code == 200
