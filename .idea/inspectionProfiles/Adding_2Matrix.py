lst1 = [[1,2,3,4],[5,6,7,8],[1,2,3,4]]

lst2 = [[1,2,3,4],[6,7,8,9],[4,5,6,7]]

lst3 = []

for i in range(3): #This represents the there are 3 lists inside it
    s = []
    for j in range(4):#This represents elements present inside the list
        r = lst1[i][j] + lst2[i][j]

        s.append(r)
    lst3.append(s)

print(lst3)

