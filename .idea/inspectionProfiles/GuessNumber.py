import random

n = random.randint(1,10)

guess = 8

while guess!=n:
    guess = int(input("Enter the guessing number"))

    if guess<0:
        print("The number is less than guessed one")

    elif guess>0:
        print("The number is greater than the guessed one")

    else:
        print("Yes you have guessed it perfectly")
