s ="bcdefghkij"
ss = sorted(s)
print(ss)

s1 =''.join(sorted(s))#if we want to get back in the form of string we need to join method
print(s1)


#To get the length of the string with considering the dots

item = input("Please enter the item name")
price = input("Please enter the price name")

total_len = len(item) + len(price)
dots = '.'*(25-total_len)

print(item+dots+price)