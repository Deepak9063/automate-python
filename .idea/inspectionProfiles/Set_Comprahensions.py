
print({s for s in range(10) if s%2==0})

my_set = {"Deepak","Deepak","suresh"}
for i in my_set:
    if i.startswith("D"):
        print(i)

#To create an empty set we use
s = set() #This creates an empty set

my_set1 = {(1,2,3,4,3,2,4,2)}
print(my_set1)
print(len(my_set1))
#Usage of discard in set where it deletes the element and also if the element is not present it dos'nt give the error message

my_set2 = {1,2,3,4,5}
my_set2.discard(5)
print(my_set2)
