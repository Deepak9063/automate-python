# String interning means address will be same for same characters in the string

s = "hello"
s1 = "hello"
print(s is s1)

print(id(s))      #These 2 strings will have same Address because both will be stored in a single memory
print(id(s1))

s3 = "Deepak"
s4 = "Deekshitha"

print(id(s3[0])) # Index value of 0 is D therefore address of both the string will be same
print(id(s4[0]))

s9 = input("please enter the string")

print(s9[0:5])
s10 = "My name is Deepak"
Last_Index = s10.split(" ")[-1]
print(Last_Index)

# Reverse a String
s11 = "My name is Deepak"
print(s11[ : :-1])