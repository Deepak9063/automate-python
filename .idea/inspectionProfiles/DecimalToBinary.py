n = int(input("Enter the number"))

bin = ''

while n>0:
    r = n%10
    n = n//10
    bin = str(r)+bin

print(bin)
