# n = int(input("Please enter the number"))
#
# # digits = str(n)
# #
# # print(len(digits))
# count = 0
# while n>0:
#     r = n%10
#     n = n//10
#
#     count = count+1
#
# print(count)

n = int(input("Please enter the number"))

count = 0
while n>0:
    r = n%10
    n = n//10
    count += 1
print(count)



