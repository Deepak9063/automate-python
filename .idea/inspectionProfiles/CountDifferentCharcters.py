s = input("Enter a String:")

low_count,up_count,num_count,sp_count = 0,0,0,0

for i in s:
    if i.islower():
        low_count += 1

    elif i.isupper():
        up_count += 1

    elif i.isnumeric():
        num_count += 1

    else:
        sp_count +=1

print(num_count,"Number Count")
print(up_count,"UpperCase Count")
print(low_count,"LowerCase Count")
print(sp_count,"Special Characters")
# count=0
# for i in s:
#     if i.isalpha():
#          low_count += i
# print(low_count)