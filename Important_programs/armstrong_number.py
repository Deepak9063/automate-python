n = int(input("Please enter the number to check weather it is armstrong or not"))

num_str = str(n)
num_of_digits = len(num_str)

sum_of_powers = sum(int(digit)**num_of_digits for digit in num_str)

if sum_of_powers == n:
    print("It is a armstrong number")

else:
    print("It is not a armstrong number")


