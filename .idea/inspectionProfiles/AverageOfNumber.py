from functools import reduce
nums = input("Enter the Numbers").split()

print(nums)

l = list(map(int,nums))
print(l)

res = reduce(lambda x,y:x+y,l)

avg = res/len(l)
print("{0:.4f}".format(avg))