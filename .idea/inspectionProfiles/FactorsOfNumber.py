n = int(input("Enter the number to find its factors"))

for i in range(1,n+1):
    if n%i == 0:
        print(i)

