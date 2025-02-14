num_of_numbers = int(input("Please enter the numbers to make it as a sum"))

count = 0
p_sum = 0
n_sum = 0

while count<num_of_numbers:
    n = int(input("Please enter the number"))
    if n>0:
        p_sum = p_sum + n


    else:
        n_sum = n_sum + n

    count += 1
    print(p_sum)
    print(n_sum)