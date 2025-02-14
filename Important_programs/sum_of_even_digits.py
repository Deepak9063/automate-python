n = int(input("Please enter the number\n"))

sum = 0
while n>0:
    r = n%10
    n = n//10
    if r%2==0:

        sum = sum+r

print(sum)