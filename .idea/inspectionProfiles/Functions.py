def add3(a,b,c):
    d = a+b+c
    return d          #If we don't write a return statement inside the function it return none
res = add3(10,20,30)
print(res)


#In functions there are 2 types of arguments (Positional Arguments) and (Keyword Arguments)

# def add3(a,b,c):
#     d = a+b+c
#     return d
# res = add3(10,20,30)     This is positional arguments
# print(res)

def add3(a,b,c):
    d = a+b+c
    return d
res = add3(c=30,b=10,a=4)  #This is keyword arguments
print(res)
