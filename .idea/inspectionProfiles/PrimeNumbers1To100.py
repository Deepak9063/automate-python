
count =0
for i in range(1,101):
    if num%i==0:
        count += 1

    if count == 2:
        print("Prime numbers between 1 to 100",i)

