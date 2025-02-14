# str = input("Please enter the string to check palindrome")
#
# rev_str = str[::-1]
#
# print(rev_str)
# if str == rev_str:
#     print("It is palindrome")
# else:
#     print("It is not a palindrome")

#string reverse
str = input("Please enter the string")
rev_str = ""
for i in range(len(str)-1,-1,-1):
    rev_str+=str[i]

print(rev_str)
if str==rev_str:
    print("It is a string palindrome")
else:
    print("It is not a string palindrome")








