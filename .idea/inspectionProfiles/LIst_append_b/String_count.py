s = "Deepak"
d = {}

for i in s:
    if i not in d:
        d[i]  = 1

    else:
        d[i] += 1

print(d)

#or we can do this by importing the counter also
from collections import Counter

s1="mississippi"

c = Counter(s1)
print(c)
