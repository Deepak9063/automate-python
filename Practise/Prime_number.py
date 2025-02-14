n = int(input("Please enter the number"))

if n == 0 or n == 1:
    print("It is neither prime nor a composite number")

count = 0
for i in range(1,n+1):

    if n%i == 0:
        count += 1
if count==2:
    print("It is a prime number")
else:
    print("It is not a prime number")







