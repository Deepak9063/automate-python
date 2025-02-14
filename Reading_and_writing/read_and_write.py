with open('example.txt','w') as file:
    file.write("Hello World\n")
    file.write("My name is Deepak\n")

with open('example.txt','r') as file:
     content = file.read()
     print(content)







