#variable length arguments

def fun1(*args):
    for i in args:
        print(i)
fun1(1,2,3,4,5)


#Keyword variable length arguments
def fun2(**kwargs):
    for x in kwargs:
        print(x,kwargs[x])

fun2(name='deepak',rollno=9900,branch='CSE')

#Mixed Arguments

def fun3(a,b,*args,**kwargs):
    print(a,b,args,kwargs)

fun3(1,2,12,13,14,15,name='Deepak',rollno=7700)
