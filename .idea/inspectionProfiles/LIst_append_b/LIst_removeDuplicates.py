lst = [1,1,2,3,4,4,5,7,7]

lst1 = []
for i in lst:
    if i not in lst1:
        lst1.append(i)

print(lst1)