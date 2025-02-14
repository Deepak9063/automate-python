s = input("Enter an expression with paranthesis")
lst = []

for i in s:
    if i=='(' or i=='{' or i=='[':
        lst.append(i)

    elif i==')' and lst[-1]=='(':
        lst.pop()

    elif i==']' and lst[-1]=='[':
        lst.pop()
    elif i=='}' and lst[-1]=='{':
        lst.pop()

    else:
        break

if len(lst)==0:
    print("Paranthesis is balanced")

else:
    print("Paranthesis not balanced")