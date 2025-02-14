
# s.remove(5)
# print(s)
# s.pop()
# print(s)
#
# d = {'name' : 'deepak','rollno':9900,'place':'tiptur'}
# for i in d:
#     print(i,d[i])

num =12345
sum = 0
while num>0:
    r = num%10
    num = num//10
    sum = sum + r
print(sum)
