# number = [1,2,3,4,6,7,8,9]
#
# n = 9
#
# sum_of_numbers = n*(n+1)//2
#
# actual_sum=0
# for i in number:
#     actual_sum += i
#
# missing_number = sum_of_numbers-actual_sum
# print(missing_number)

number = [1,2,3,4,5,6,7,9]
n = 9
sum_of_number = n*(n+1)//2
actual_sum = 0
for i in number:
    actual_sum += i

missing_number = sum_of_number-actual_sum
print("The missing number is",missing_number)
print(actual_sum)




