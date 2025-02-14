import requests

head = {
    "Content-Type": "application/json",
    "Authorization" : "Bearer e31000ad8b55600da48617a5bae98246e38f9c6d36e068785b16f38ae5207f41"
}

request_payload  = {


      "name": "Deepak123",
      "email": "deepakshetty125371@gmail.com",
      "gender": "male",
      "status": "inactive"
}

url = "https://gorest.co.in/public/v2/users"
response = requests.post(url,json=request_payload,headers=head)

print(response.json())

assert response.status_code==201

getResponse = requests.get(url+'/'+str(response.json()['id']),headers=head)

print("2nd",getResponse.json())



