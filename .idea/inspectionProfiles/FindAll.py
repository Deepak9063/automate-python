#Instead of search and match function we use findAll function
import re

text = "Python is super easy."
regex = r"\."

l = re.findall(regex,text)
print(l)

#usage of |(or) meta character

regex1 = r"Python|super"

l1 = re.findall(regex1,text)
print(l1)

'''Usage of meta characters
    (*) It is used for 0 or many
    (.) Single meta character
    (\) It is used as escape[Used in special cases]
    (?) 0 0r many characters
    (+) 0 or 1 characters'''

text1 = "hhow is how the hhhow"
regex2 = r"h*ow"

l2 = re.findall(regex2,text1)
print(l2)
print("Number of occurances",len(l2))




