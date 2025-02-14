lst = [1,5,4,3,7,8,9]

for i in lst:
    for j in range(i+1,len(lst)):
        if lst[i] < lst[j]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp



print(lst)