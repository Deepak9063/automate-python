count = 0

while count<10:
    n = int(input("Enter a number"))

    if n%3==0:
        continue
    print(n)
    count = count + 1
