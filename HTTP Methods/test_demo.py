import pytest
import requests

def test_getrequest_validation():
    header = {
        'Content-Type' : 'application/json'
    }

    base_url = 'https://reqres.in/'

    response  = requests.get(url=str(base_url+'api/users/2'),headers=header)
    assert response.status_code == 200
    print(response.json())


