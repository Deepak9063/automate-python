num = int(input("Please enter the number to check weather it is prime or not"))

count =0
for i in range(1,num+1):
    if num%i == 0:
       # print(i)
        count += 1

if count ==2:
    print("It is a prime number")

else:
    print("It is not a Prime number")