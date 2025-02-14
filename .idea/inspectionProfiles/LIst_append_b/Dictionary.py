#This dictionary contains the key value pair

dict1 = {'deepak':'Tiptur','manoj':'Banglore','shashank':'somenahalli'}

print(dict1['manoj'])

#To iterate over the dictionary
for i in dict1:
    print(i,dict1[i])


dict1 = ((1,2),(3,4),(5,6),(7,8))
print(dict1)

dict1 = dict(dict1) #where this converts tuple of tuples into dictionary
print(dict1)

#Using zip function
set1 = {1,2,3,4}
str = 'ajkl'

dic22 = dict(zip(set1,str))
print(dic22)


set2 = {3,4,5,6}
str1 = 'abcd'
dict3 = dict(zip(set2,str1))
print(dict3)