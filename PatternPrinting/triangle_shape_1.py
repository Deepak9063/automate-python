star = 1
space = 3

for i in range(1,4):
    for k in range(1,space):
        print(" ",end=" ")


    for j in range(1,star+1):
        if i == 3 and j == 5:
            print("2",end=" ")
        else:

            print("1",end=" ")

    print()
    star = star+2
    space = space-1