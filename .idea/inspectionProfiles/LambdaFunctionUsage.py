# in lambda function we use in some of the special cases when we use FILTER,REDUCE and MAP function

'''lst = [20,19,18,17,16,15]
def fun(x):
    if x%2==0:
        return True
    else:
        return False

even_lst = list(filter(fun,lst))  #we should use TypeCasting
print(even_lst)'''


# use lambda function
lst = [20,19,18,17,16,15]
evn_lst = list(filter(lambda x : x%2==0,lst))
print('Usage of filter function')
print(evn_lst)

# Usage of reduce function
from functools import reduce

lst1 = [1,2,3,4,5]
res = reduce(lambda x,y : x+y,lst1)
print("usage of reduce function")
print(lst1)

# Lambda function in association with Map

lst2 = [1,2,3,4,5,6,7]
res1 = list(map(lambda x : x**2,lst2))
print('Usage of map function')
print(res1)

'''def fun1(num):
    return lambda x: x*num

math_table = fun1(6)
for i in range(1,11):
    print(math_table(i))'''

#Instead of hardcoding take the input from the user
def fun1(num):
    return lambda x : x*num
n = int(input("Enter the number:\n"))
math_table = fun1(n)
for i in range(1,11):
    print("Usage of lambda function inside a another function")
    print(n," x ",i,"=",math_table(i))



