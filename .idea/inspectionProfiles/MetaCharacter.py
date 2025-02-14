import re

text = "My name is Deepak090920939209"  #Usage of meta charcter

regex = r"."

match = re.findall(regex,text)
print(match)  #In this space is also considered it considers everything

# Matching all the alpahbets present in the string

regex1 = r"[a-zA-Z0-9]"  #This type of matching is known as character class matching

match1 = re.findall(regex1,text)
print(match1)

# Instead of writing all these we can consider the alphanumeric characters by using (\w)
regex2 = r"\w"      #This \w plays a very important role in pattern matching
match3 = re.findall(regex2,text)
print(len(match3))

print(''.join(match3))

regex4 = r"[a-zA-Z]"

match4 = re.match(regex4,text)

print("My match",match4.group())




# to match only lowerCase use \d
# to match only uppercase use \D
# to match only spaces use \s
# to match non-space characters \S(UpperCase)
# to match continiously two vowels[a,e,i,o,u]{2}
''' to create a word boundary \babc\b where it matches only when abc is present for this we should use findall function instead 
of search function where search function only finds the which will be matched at the starting'''
