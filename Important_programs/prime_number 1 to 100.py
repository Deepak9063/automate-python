#num = int(input("Please enter the number between 1 to 100"))
count1 = 0
count2  = 0

for num in range(1,101):
    count = 0
    for i in range(1,num+1):
        if num%i==0:
            count = count + 1

    if count == 2:
        print("It is a prime number",num)

        count1 += 1


    else:
        print("It is not a prime number",num)

        count2 += 1

print("Total number of prime numbers",count1)
print("Total number of non prime numbers",count2)








