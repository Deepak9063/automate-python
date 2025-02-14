lst1 = [1,2,3,4,5,6,7]
lst2 = [2,4,6,7,8,9]
lst3 = []

for i in lst1:
    if i in lst2:
        lst3.append(i)
print(lst3)


