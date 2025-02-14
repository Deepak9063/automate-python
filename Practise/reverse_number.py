# num = 12344321
#
# rev=0
# original_num = num
#
# while num>0:
#     digit = num%10
#     rev = rev*10+digit
#     num = num//10
#
# print(rev)
# if rev == original_num:
#     print("It is a palindrome")
#
# else:
#     print("It is not a palindrome")

# list = [1,3,4,2,5,6,7,8]
# for i in range(0,len(list)):
#     for j in range(i+1,len(list)):
#         if list[i] > list[j]:
#             temp = list[i]
#             list[i] = list[j]
#             list[j] = temp
#
# print(list)

# lst = [0,1,2,3,4,5,6,7]
# count = 0
#
# for i in range(0,len(lst)):
#     if lst[i]==0 or lst[i]==1:
#         print(f"{lst[i]} It is not a prime number")
#
#     if lst[i]%i==0:
#         count +=1
#
#         if count==2:
#             print(f"{lst[i]} It is a prime number")
#
#         else:
#             print(f"{lst[i]} It is not a prime number")
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
#
# prime_numbers = [num for num in lst if is_prime(num)]
#
# print("Prime numbers in the list:", prime_numbers)


lst = [1,"2","name",-3.07,True]

for i in range(0,len(lst)):
    print(type(lst[i]))


l1 = [2,4]
for k in range(0,len(l1)):
    n=l1[k]

    if n==0 or n==1:
        print("It is not a prime number")
    count = 0
    for i in range(1,n+1):
        if n%i==0:
            count += 1

    if count == 2:
        print("It is a prime number")

    else:
        print("It is not a prime number")













