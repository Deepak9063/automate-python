lst1 = [1,2,3,4,5,6,7]
lst2 = [9,10,1,2,3,4,40]

for i in lst2:
   if i not in lst1:
       lst1.append(i)
print(lst1)


#we have both built-in functions  aswell as methods