import requests
import json
def add_new_data():
    URL = "http://localhost:3000/students"
    data = {
        "name": "deepak",
        "location": "AJP",
        "phone": "789211"
    }

    response = requests.post(URL,json=data)
    response_json = response.json()

    assert response.status_code==201,"Student data is not been updated so the status code is 201"
    id = response_json.get('id')
    print(f"Student ID is {id}")
    return id
def update_new_data(id):
    print(id)

    URL = f"http://localhost:3000/students/{id}"
    data = {
        "name": "deepak12",
        "location": "tiptur",
        "phone": "968619"
    }
    response = requests.put(URL,json=data)
    response_json = response.json()
    print(response_json)

updated_id= add_new_data()
update_new_data(updated_id)


