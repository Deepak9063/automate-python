x=99

def fun():
    print(globals())
    global x    # if both local and global variables are having same name we should use this...
    x=999
    print(x)
fun()
print(x)