#If we create the empty list,if we append the list size gets increased
def add_item(item,L = []):
    L.append(item)
    return L
print(add_item(22))
print(add_item(44))


#Here element gets inserted at the last to the list L1
L1 = [1,2,3,4,5]
add_item(6,L1)
print(L1)

L1.append(3)
print(L1)


