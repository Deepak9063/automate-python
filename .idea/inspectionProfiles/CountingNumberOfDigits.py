n = int(input("Please enter the number"))

counter = 0
while n>0:
    n = n//10
    counter = counter + 1
print("The number of digits are",counter)

