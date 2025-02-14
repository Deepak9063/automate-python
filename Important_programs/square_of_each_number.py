n = int(input("Please enter the number"))

square = []

while n>0:
    r = n%10
    n = n//10

    square.append(r**2)
square.reverse()

print(square)


