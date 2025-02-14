s  = input("Enter the String:") # conversion from lower case to upper case....

s_upper = ""
for i in s:
    if ord(i)>=97 and ord(i)<=122:
        s_upper += chr(ord(i)-32)
    else:
        s_upper = s_upper + i

print(s_upper)

