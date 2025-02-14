t1 = [x for x in  range(10)]
print(t1)

t2 = tuple(x for x in range(10))#creation of comprahension using tuple function
print(t2)

t3 = (*(x for x in range(10)),)#we can create a comprahension like this also we should have (,) at the end

str = "         My name is deepak          "

print(str.strip())  #This strip function is used to remove the white spaces

t4 = (*(x for x in 'ZyYhon' if x.islower()),)
print(t4)

t5 = tuple(x**2 for x in range(2,9,))
print(t5)

