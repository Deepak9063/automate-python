# lst  =[10,5,6,8,6,5,43]
#
# n = len(lst)
#
# for i in range(n):
#     swapped = False
#
#     for j in range(0,n-i-1):
#         if lst[j] > lst[j+1]:
#             lst[j],lst[j+1] = lst[j+1],lst[j]
#
#             swapped = True
#
#         if not swapped:
#             break
#
# print(lst)

# lst = [1,4,3,2,5,6,7]
#
# for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i]>lst[j]:
#             temp = lst[i]
#             lst[i] = lst[j]
#             lst[j] = temp
#
# print(lst)

list = ["a","b","e","d","n","i"]

for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if ord(list[i]) > ord(list[j]):
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
print(list)


