dict1 = {'deepak':'Tiptur','manoj':'Banglore','shashank':'somenahalli'}

#In this dictionary where iteration takes like this where both index i and dict[i] gets printed
for i in dict1:
    print(i,dict1[i])


#Usage of get method in the dictionary,where it has key and value if key is entered then we get value as output
print(dict1.get('deepak'))

# we can get values by entering the key without using get
print(dict1['deepak'])
#In this if the key is not present then it gives error

print(dict1.keys())
print(dict1.values())

# Usage of update function
dict2 = {1:'deepp',2:'man',3:'women'}
dict3 = {6:'deepp',5:'man',4:'women'}

#In this dictionary 2 has been updated
dict2.update(dict1)
print(dict2)

#Set default method

dict1.setdefault(8) # If the value is not there then by default it sets the value
print(dict1)
