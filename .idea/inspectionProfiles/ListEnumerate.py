#This enumerate method gives both index value aswell as the values present in it

lst = [1,2,3,4,5,6]

for i,j in enumerate(lst):
    print(i,j)

print("This is when iterating using for loop\n ")
print('')

for i in range(len(lst)):
    print(i,lst[i])