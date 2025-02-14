#In this shallow copy both original list aswell as the shallow_copied list will be changed


import copy
lst1 = [[10,20],[30,40]]

shallow_copy = copy.copy(lst1)
print(lst1)
print(shallow_copy)
print(lst1 is shallow_copy)

lst1.append([50,60])
print(lst1)
print(shallow_copy)
lst1[1][0] = 300
print(lst1)
print(shallow_copy)

#for deep copy the original list retains the same and it does'nt get changed only list where
print("From here it works on deep coppy")
lst2 = [[10,20],[30,40]]
deep_copy = copy.deepcopy(lst2)
print(lst2)
print(deep_copy)
lst2.append([50,60])
print(lst2)
print(deep_copy)
lst2[1][0] = 300
print(lst2)
print(deep_copy)