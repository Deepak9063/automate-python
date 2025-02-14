lst = ['A','B','C','A','B','E','G','A','N']

res_count = []

# for i in lst:
#     if i not in res_count :
#         res_count.append(i)
#
#         count = lst.count(i)
#         res_count.append(count)
#
# print(res_count)
for i in lst:
    if i not in res_count:
        res_count.append(i)

        count = lst.count(i)
        res_count.append(count)
print(res_count)
