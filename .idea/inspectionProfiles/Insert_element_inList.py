lst = eval(input("Enter the element in the form []"))
n = int(input("Enter the value to be inserted"))

print(lst)

for i in range(len(lst)):
    if n<lst[i]:
        lst.insert(i,n)
        break
print(lst)