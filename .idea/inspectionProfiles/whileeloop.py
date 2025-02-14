'''n = int(input("Please enter the number"))

while n>0:
    r = n%10
    n = n//10
    print(r)'''

n = int(input("Please enter the Number"))
counter = 1

while counter<=10:
    print(n,"*",counter,"=",counter*n)
    counter = counter +1
