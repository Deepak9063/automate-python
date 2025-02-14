list = ['burger','pizza','coke','apple']

for i in list:
   if i.startswith('b'):

      print(i)

for j in list:
   if j.startswith('p'):
      print(j)


#This is how the extend works
list1 = [1,2,3,4]
list2 = [5,6,7,8]

list1.extend(list2)
print(list1)




