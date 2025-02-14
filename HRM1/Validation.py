import time

import requests
from HRM1.url import base_url,head,get_leave,post_leave
from HRM1.pay_load import post_data,put_leave

class Validate:
    def get_url(self):
        start_time = time.time()
        url = f'{base_url}/{get_leave}'
        response = requests.get(url,headers=head)
        end_time = time.time()
        response1 = response.json()
        print(response1)
        response_time = end_time-start_time
        print(response_time)
        expected_time=5.0

        assert response.status_code==200,"Unexpected"
        assert "id" in response1,"ID not found"
        assert response1['id']==108,"Id value is different"
        assert "email" in response1,"Email not found"
        assert "displayName" in response1,"Display name is not present"
        assert response1['displayName']=="Deepak T M","Display name is different"
        assert "tempAddress" in response1,"TempAddress not found"
        assert "permanentAddress" in response1,"permanent address not found"
        assert "city" in response1,"City is not found"
        assert "state" in response1,"State is not found"
        assert "pinCode" in response1,"pincode is not found"
        assert "mobileNumber" in response1,"mobile number not found"
        assert "userStatus" in response1,"username not found"
        assert response_time<=expected_time,"bad response time"




    def post_url(self):
        url = f'{base_url}/{post_leave}'
        response = requests.post(url,headers=head,json=post_data)
        response1 = response.json()
        print(response1)
        print(response.status_code)


        id = response1.get("id")
        print(id)
        assert "id" in response1,"Id not found"
        assert response1["id"]==id,"Id is not same"
        assert "leaveType" in response1,"leaveType not found"
        assert "leaveTo" in response1,"leaveTo not found"
        assert response1["leaveType"]=="Other leave","reason is not valid"
        assert isinstance(response1["id"],int),"Id is not in Integer"
        assert isinstance(response1["status"],str),"Status is not in integer"
        assert response1["status"]=="Submitted","It is not been submitted"
        assert response1["unit"]==2.0,"unit is not 2.0"
        assert response1["year"]==2024,"year is not 2024"
        assert response1["month"]=="OCTOBER","The month is not valid"
        assert response1["email"]=="deepak.tm@lirisoft.com"
        return id
    def put_url(self,id):
        url = f'{base_url}/{post_leave}/{id}'
        response = requests.put(url,headers=head,json=put_leave)
        response1 = response.json()
        print(response.text)

        assert "id" in response1,"Id not found"
        assert "reason" in response1,"Reason not found"
        assert "department" in response1,"Department is not found"
        assert "month" in response1,"Month not found"
        assert "email" in response1,"Email not found"
        assert response1["id"] == id,"ID is not same"
        assert isinstance(response1["id"],int),"Id is not integer"
        assert isinstance(response1["status"],str),"Status is not string"
        assert isinstance(response1["department"],str),"Status is not String"
        assert isinstance(response1["year"],int),"year is not in integer"
        assert isinstance(response1["month"],str),"month is not in string"
        #assert isinstance(response1["email"]),"email is not in string"





    def delete_url(self,id):
        url = f"{base_url}/{post_leave}/{id}"
        response = requests.delete(url,headers=head)
        #response1 = response.json()
        #print(response1)
        print(response.status_code)

obj = Validate()
obj.get_url()
id1=obj.post_url()
obj.put_url(id1)
obj.delete_url(id1)



















