import re

text = '''gogle
        google
        gooogle
        goooogle
        goooooogle
        gooooooogle'''

regex = r"go{2,4}le"

l = re.findall(regex,text)
print(l)
print(len(l))

# usage of ^(matches with starting char) and $(matches with ending char) symbol
text1 = "python is a language and it is  not a snake"
regex1 = r"^python"

match = re.search(regex1,text1)
print(match)

a = 20
print(hex(a))



