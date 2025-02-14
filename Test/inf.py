#Explain method overloading
# class Sum:
#     def sum(self,*args):
#         result = 0
#         for num in args:
#             result += num
#         return result
#
# sum_obj = Sum()
# print(sum_obj.sum(1,2,3,4))
# print(sum_obj.sum(1,2))

#method overriding
# class Animal:
#     def animal_sound(self):
#         print("Animal makes sound")
#
# class Cat(Animal):
#     def animal_sound(self):
#         print("Cat says 'Meow'")
#
# class Dog(Animal):
#     def animal_sound(self):
#         print("Dog says 'Meow'")
#
# dog_obj = Dog()
# dog_obj.animal_sound()
# cat_obj = Cat()
# cat_obj.animal_sound()

#Constructor

# class Area:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def square(self):
#         result = self.a + self.b
#         return result
#
#     def rectangle(self):
#         result = 2 * self.a * self.b
#         return result
#
# area_obj = Area(2,5)
# print(area_obj.square())
# print(area_obj.rectangle())

#prime number b/w  1 to 100

# prime_count = 0
# non_prime_count = 0
# for num in range(1,101):
#     count = 0
#     for  i in range(1,num+1):
#         if num%i==0:
#             count += 1
#     if count == 2:
#         prime_count += 1
#         print(num,"It is a prime number")
#
#     else:
#         non_prime_count += 1
#         print(num,"It is not a prime number")
#
# print("Total number of prime numbers are",prime_count)
# print("Total number of non prime numbers",non_prime_count)

#prime numbers
# num = int(input("Please enter the number"))
# count = 0
# for i in range(1,num+1):
#     if num%i==0:
#         count += 1
#
# if count == 2:
#     print("It is a prime number")
#
# else:
#     print("It is not a prime number")
#
# lst = [1,2,3,4,5,6]
# sum = 0
# for i in range(0,len(lst)):
#     if lst[i]%2==0:
#         sum += lst[i]
#
# print(sum)

# num = 123456
# sum = 0
# while num>0:
#     r = num%10
#     if r%2==0:
#         sum += r
#     num = num//10
# print(sum)

#Bubble sort
# lst = [1,2,6,5,4,3,7]
#
# for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#         if  lst[i]>lst[j]:
#             temp = lst[i]
#             lst[i] = lst[j]
#             lst[j] = temp
#
# print(lst)


#Lambda function
result = lambda x,y:x+y
print(result(3,4))

result1 = lambda a,b:a+b
print(result1(7,8))





















