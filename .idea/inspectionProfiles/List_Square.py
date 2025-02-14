lst = [2,4,6,8,9,11,13,15]

sq_lst = []

for i in lst:
    sq_lst.append(i**2)

print(sq_lst)

#we can write this code using listComprahension also

sq1_list = [i**2 for i in lst]
print(sq1_list)

#Print the square of a number only if it is a even number

sq_even = [i**2 for i in lst if i%2==0]
print(sq_even)
