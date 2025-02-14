# n = int(input("Please enter the number"))
# reverse = 0
# original_num = n
#
# while n>0:
#     r = n%10
#     reverse = reverse*10+r
#     n = n//10
# print(reverse)
# if reverse == original_num:
#
#     print("it is  palindrome")
# else:
#     print("It is not a palindrome")
#
#
n = int(input("Please enter the number"))
reverse = 0
original_num = n
while n>0:
    r = n%10
    reverse = reverse*10+r
    n = n//10
print(reverse)

if reverse == original_num:
    print("It is a palindrome")

else:
    print("It is not a palindrome")



#Palindromic string




