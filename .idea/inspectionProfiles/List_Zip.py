lst1 = [1,2,3,4,5,6]
lst2 = [7,8,9,0]

print(list(zip(lst1,lst2)))

# To iterate b/w two list at a time we can use zip function

for i,j in zip(lst1,lst2):
    print(i,j)

