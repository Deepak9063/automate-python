odd_sum,even_sum = 0,0

n = int(input("Enter the number:"))

for i in range(1,n+1):
    if i%2==0:
        even_sum += i
        continue

    else:
        odd_sum += i


print("Even sum is ",even_sum)
print("Odd sum is ",odd_sum)