String = input("Please enter the string to check weather it is palindrome or not : \n")

rev = String[::-1]
if String == rev:
    print("The given string is palindrome")
else:
    print("The given string is not palindrome")