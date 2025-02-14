email = input("Please enter the mailId")

atrate = email.index('@')

print("User Id : ",email[:atrate])
print("Domain name : " ,email[atrate+1:])

