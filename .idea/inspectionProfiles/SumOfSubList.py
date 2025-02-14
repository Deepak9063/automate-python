lst = input("Enter the list in form []\n")



lst = eval(lst)

start = int(input("Enter the Start Index"))
stop = int(input("Enter the StopIndex"))

print("sum =",sum(lst[start:stop+1]))