for i in range(0,4):
    for j in range(0,4):
        print("*",end="")

    print()


for i in range(1,6):
    for j in range(1,i):
        print("*",end="")

    print()
print("next program")


star = 7
space = 0
for i in range(1,5):
    for k in range(1, space + 1):
        print(" ", end=" ")

    for j in range(1, star + 1):
        print("*", end=" ")


    print(" ")
    star = star -2
    space = space+1


