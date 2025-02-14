import re

text = "Python is a very good language"

regex = r"Python" #r is used to create a raw string
match = re.match(regex,text)
print(match)
start,end = match.span()

print(text[match.start():match.end():])

#match function only matches if it is present in the begining of the string

#instead of match function we can use search function

regex1 = "good"

match1 = re.search(regex1,text)

print(text[match1.start():match1.end():])



