s = "Hello how are you"

print(s.find('o',2,7)) #usage of s find method

#rfind method it starts searching in the reverse direction

print(s.rfind('u'))

# casefold method is used for case insensitive methods whare it converts all the characters to lowercase

print(s.casefold())

# Regarding case sensitive we have *upper,lower,title,casefold

#we have one more that is (swapcase) where it converts lower to upper and upper to lower case

print(s.isalnum())#where it checks weather contains both alphabets and characters
print(s.isalpha())#where it checks that it contains only alphabets

print(s.isidentifier())# checks for the given string has the valid variable name

#we have some more methods such as removing the substrings such as remove suffix and remove prefix

# we have some more methods such as rpartition


print(s.rpartition('r'))

# we have replace method(In this we repalce old with new one)

s1 = 'a,b,c,d,e'
print(s1.replace(',','-',3))#in last we can specify that how many we want to repalce

#Join method
s2='/'
print(s1.join(s2))

# we have another method called split() by default it splits by the spaces
print(s1.split(","))

#wehave one method we split it by lines
print(s.splitlines())
