# lst = ["a","c","f","b","z","w"]
#
# for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#         if ord(lst[i]) > ord(lst[j]):
#             temp = lst[i]
#             lst[i] = lst[j]
#             lst[j] = temp
#
# print(lst)

lst1 = [0,2,4,3,5,6]

for i in range(0,len(lst1)):
    for j in range(i+1,len(lst1)):
        if lst1[i]>lst1[j]:
            temp = lst1[i]
            lst1[i] = lst1[j]
            lst1[j] = temp

print(lst1)



    