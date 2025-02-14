l1 = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]

trans_matrix = []

for i in range(4):
    s = []
    for j in range(3):
        s.append(l1[j][i])

    trans_matrix.append(s)

print(trans_matrix)


