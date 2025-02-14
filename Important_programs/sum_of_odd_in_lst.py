input_str = input("Please enter the string by leaving single space")

lst = [int(x) for x in input_str.split(" ")]
sum_of_odd=0

for i in lst:
    if i%2!=0:
        sum_of_odd += i

print(sum_of_odd)

