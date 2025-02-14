# def sum(a,b):
#     c = a+b
#     return c
#
# res = sum(10,20)
# print(res)


# reversing string

#s = "My name is deepak"

#word = s.split(" ")[::-1]

#print(word)
# for i in range(len(word)-1,-1,-1):
#
#
#     print(word[i],end=" ")
#
# print()

# l = [1,2,3,4,5,6]
# l1 =[]
# for i in range(len(l)-1,-1,-1):
#     l1.append(l)
# print(l1)
#
# #Factorial of a number
# n = int(input("Please enter the number"))
# fact = 1
# for i in range(1,n+1):
#     fact = fact*i
#print(fact)

#Reversing the string
# str = "My name is Deepak"
# rev_str= ""
# str_split = str.split(" ")
# for i in range(len(str_split)-1,-1,-1):
#     rev_str += str_split[i]+" "
#
# print(rev_str)

#Reversing the string of the particular word
# str = "My birth place is Tiptur"
# rev_str = ""
# str_split = str.split(" ")
#
# for i in range(len(str_split)-1,-1,-1):
#     if i==2:
#         word=str_split[i]
#         rev_word = ""
#         for i in range(len(word)-1,-1,-1):
#             rev_word += word[i]
#         rev_str+=rev_word + " "
#     else:
#         rev_str+=str_split[i] + " "
#
# print(rev_str)

#Fibonacci series
# n = int(input("Please enter the number"))
# a=0
# b=1
# for i in range(n):
#     print(a)
#     c = a+b
#     a=b
#     b=c


#Inheritance
# class Animal():
#     def lion(self):
#         print("It is a lion")
#     def tiger(self):
#         print("It is a Tiger")
#
# class Herbivorus(Animal):
#     def cat(self):
#         print("It is cat")
#     super().tiger()
#     super().lion()
#
# herb = Herbivorus()
# herb.lion()
# herb.cat()
# herb.tiger()

#Constructor
# class Construct:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#
#     def add(self):
#         c = self.a+self.b
#         return c
#
# con = Construct(2,5)
# res = con.add()
# print(res)

#Palindrome
# num = int(input("Please enter the number"))
# original_num = num
# rev=0
#
# while(num>0):
#     r = num%10
#     rev = rev*10+r
#     num=num//10
#
# print("Reverse of a number is",rev)
# if rev==original_num:
#     print("It is a Palindrome")
# else:
#     print("It is not a palindrome")


#Bubble sort
# lst = [1,4,3,2,5,6]
# for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i]>lst[j]:
#             temp = lst[i]
#             lst[i] = lst[j]
#             lst[j] = temp
# print(lst)

#Find the missing number
# lst = [1,2,3,4,5,6,8,9]
# n = 9
# sum=0
# total_sum = n*(n+1)//2
# for i in range(0,len(lst)):
#     sum = sum+lst[i]
#
# missing_number = total_sum-sum
# print(missing_number)

#
# lst = [1,2,3,4,5,6]
# rev_lst = lst[::-1]
# print(rev_lst)


#Prime numbers in the range of 1 to 100

# class Prime:
#
#     def prime(self):
#         prime_count = 0
#         not_prime_count = 0
#         for num in range(1,101):
#             count=0
#             for i in range(1,num+1):
#                 if num%i==0:
#                     count += 1
#
#             if count==2:
#                 prime_count += 1
#
#
#             else:
#                 not_prime_count += 1
#         return not_prime_count,prime_count
#
#
# p = Prime()
# prime_count,not_prime_count = p.prime()
# print("Number of prime count between 1 to 100 is ",prime_count)
# print("Number of not prime count between 1 to 100 is ",not_prime_count)

class Prime:
    def prime(self):
        prime_count = 0
        not_prime_count = 0
        for num in range(1,101):
            count = 0
            for i in range(1,num+1):
                if num%2==0:
                    count+=1

                    if count==2:
                        prime_count += 1
                    else:
                        not_prime_count+=1
            return prime_count,not_prime_count

print("Prime number count is",)


























