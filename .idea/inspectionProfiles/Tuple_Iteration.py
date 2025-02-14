tuple = [1,2,3,4,5,6,7] #Tuples are immutable they does'nt allow any sort of modification
for i in tuple:
    print(i)

print("This seperates the 2 codes\n")

for i in range(len(tuple)):
    print(tuple[i])

t1 = tuple + ([1,2,3,4,5])
print(t1)

tuple1 = ('deepak',1,'dee',3.142)
if 'deepakkk' in tuple1:
    print("String is Present")
else:
    print("String is not present")

str = [('deepak','manoj','suresh','ramesh')]




