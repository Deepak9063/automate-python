import requests

para = {
    'page' : 1,
    'per_page' : 1
}

url = "https://reqres.in/api/users"
response = requests.get(url,params=para)

print(response.json())

assert response.status_code == 200


