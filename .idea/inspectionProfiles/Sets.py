# In sets it does'nt have indexing aswell it does'nt contain the duplicates
s = {1,2,3,4,5,6,7,8,8,8,8}
print(s)

s2 = set('python')   #These sets does'nt keep the elements in the ordered fashion
print(s2)

s4 = {'Python'}
print(s4)

l1 = [1,2,3,3]  #we can replace the elements in the list but this is not possible in the sets
l1[1] = 4
print(l1)

#we can replace the elements by discarding the values
s3 = {1,2,3,4,5,6,7}
s3.discard(2)
print(s3)

s3.add(200)  #In this set insertion the value can be inserted any where in the set
print(s3)

s3.add(7)  #If we add duplicate values it does'nt get printed
print(s3)