for i in range(0,5):
    for j in range(0,5):
        if i>=j:
            print("*",end=' ')
    print('')

print('')

for i in range(0,5):
    for i in range(0,5):
        print("* ",end=' ')

    print('')

# In a single for loop itself we can do with the star printing
print('')

for i in range(5,0,-1):
    print("* "*i)

print("abc\aaasfff")