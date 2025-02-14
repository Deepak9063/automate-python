
#This is how the iterators work in this

L = ['sun','mon','tue','wed','thur','sat']

itr = iter(L)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
#print(next(itr)) #It generates the error when it exceeds the element present in the list



print("From here iterators start working\n")
#This is how the generators work
def days():
    L1 = ['sun','mon','tue','wed','thur','sat']
    i=0

    while True:
        x = L[i]
        i = (i + 1)%7
        yield x

d = days()
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))






