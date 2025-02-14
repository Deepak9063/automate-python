lst = [10,(20,20,40,59),{1,2,3,4,6},{'x':1,'y':2}]
print(lst)
print(lst[1][2])

#Sets cannot be accessed using index values

lst1 = [0]*10
print(lst1)

# Using for loop

for i in range(0,len(lst)):
    print(lst[i])

    #or

for i in lst:
    print(i)


thislist = ["apple", "banana", "cherry"]  #where it replaces banana and cherry with watermelon
thislist[1:3] = ["watermelon"]
print(thislist)

#Addinmg the elements to the list
ele = [1,2,3,4,5,6,7]
ele.append([60])    #we append inside a list it will give list inside a lst as output
print(ele)

#To get rid of list inside list we should use concat instead of that

ele = ele + [10,20,30,40,50]
print(ele)

#we can use extend also so that it is iterable we can add elements to it
ele.extend([90,100,200,300])
print(ele)

#Removing the elements in the list
element = [10,20,30,40,50,30] #In this we have to remove the element 30
element.remove(30)
print(element)   #Here only first 30 will be deleted we want to delete 2nd one also

#So we have implement loops to delete the 2nd 30 also

while 30 in element:
    element.remove(30) # In this whereever 30 comes it will be deleted

print(element)

# Usage of delete and pop

data = [1,2,3,4,5,6,7]
data.pop(3)
print(data)

#Usage of delete where using slicing we can delete how many ever elements we want
del data[2:6]
print(data)
