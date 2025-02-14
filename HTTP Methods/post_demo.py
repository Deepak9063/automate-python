import requests
import json

base_url = "https://reqres.in"

headers_test = {'Content-Type' : 'application/json'}

# pay_load = {
#     'name' : 'deepak',
#     'job' : 'QA'
# }

#when we want to give the payload in json file we should create like this
json_file = open('users.json')
json_payload = json.load(json_file)



# response = requests.post(url=base_url+'/api/users',headers=headers_test,json=json_payload)
# print(response.status_code)
# print(response.text)




