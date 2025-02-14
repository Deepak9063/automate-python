num = int(input("Enter the number to find its fibonnaci series"))

a = 0
b = 1

for i in range(num):
    print(a)         # This is used for printing the first term
    c = a+b
    a = b
    b = c

