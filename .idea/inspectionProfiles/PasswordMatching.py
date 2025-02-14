pass1 = input("Please enter the Password")
pass2 = input("Please confirm the password")

if pass1==pass2:
    print("Both the passwords are matching")
else:
    if pass1.casefold()==pass2.casefold():
        print("Please consider the cases and recheck the password")

    else:
        print("Password is incorrect")

