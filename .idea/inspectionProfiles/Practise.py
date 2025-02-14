def mul(x,y):
    c = x*y
    print(c)

mul(3,4)


def addition(x,y):
    c = x+y
    return c
rse = addition(3,4)
print(rse)

def div():
    x=10
    y=2
    c=x/y
    return c
res = div()
print(res)

def pow_of(x=2,y=3):
    c = x**y
    print(c)
pow_of()

def pizza_toppings(toppings):
    print(toppings)
pizza_toppings("cheese")

#variable length argument where * represents variable length argument
def pizza_variable(*toppings):
    print(toppings)
pizza_variable("cheese","butter","corn","sauce")

# 2 arguments one with variable length and another one with one

def pizza_twoArguments(*toppings,number):  #we have specify the arguments for the second arguments
    print(toppings)
    print(number)
pizza_twoArguments("corn","nuggets","cashew",number="four")

#variable length keyword arguments
def student_data(**data):  #It has two stars because to assign arguments with values
    print(data)
    print(type(data))
student_data(name='Deepak',age=23,Gender='M')

import math
help(math)

def sum():
    a=10
    b=20
    c=30
    return a,b,c
res1,res2,res3 = sum()
print(res1)
print(res2)
print(res3)

def add():     #It gives the output in the form of tuple
    a=10
    b=20
    c=30
    return a,b,c
res = print(add())
