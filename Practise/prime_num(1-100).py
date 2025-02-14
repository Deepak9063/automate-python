# prime_count = 0
# non_prime_count = 0
#
# for num in range(1,101):
#     count  = 0
#     for i in range(1,num+1):
#         if num%i==0:
#             count += 1
#
#     if count == 2:
#         print(num,"It is a prime number")
#         prime_count += 1
#
#
#     else:
#         print(num,"It is not a prime number")
#         non_prime_count += 1
#
# print(prime_count)
# print(non_prime_count)
#

lst=[1,4,3,5,6,7,8,9]
lst_length = len(lst)
for i in range(0,len(lst)):
    if lst_length%2==0:
        print("If its even this gets printed")
        print((lst_length//2)-1,lst_length//2)
    else:
        print("If its odd this gets printed")
        print(lst_length//2)








