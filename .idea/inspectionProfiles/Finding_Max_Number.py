num_of_numbers = int(input("Enter the number of numbers "))

max = 0
count = int(input("Enter the num"))

while count<num_of_numbers-1:   # -1 is taken because since the first number of the count is taken as the input
    n = int(input("Enter the number"))

    if n>max:
        max = n
        count = count + 1

print(max)

