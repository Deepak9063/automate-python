# lst = [1,2,3,4,5,6]
#
# for i in range(len(lst)-1,-1,-1):
#     print(lst[i])
#
# lst.insert(3,7)
# print(lst)
#
# lst.pop()
# print(lst)
#
# t1 = (1,2,3,4,5)
# t2 = (5,6,7,8,9)
#
# t3 = t1+t2
# print(t3)

str = "123ABC#*&^"

str_alphabets = ""
str_numeric = ""
str_specialchar = ""

for i in str:
    if i.isalpha():
        str_alphabets += i


    elif i.isnumeric():
        str_numeric += i


    else:
        str_specialchar += i


print("Alphabets :",str_alphabets)
print("Numeric :",str_numeric)
print("SpecialChar :",str_specialchar)





