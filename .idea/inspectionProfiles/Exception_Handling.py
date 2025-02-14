L = [10,20,30,40,50]
index = int(input("Enter the index"))
# try:
#     print(L[index])
# except IndexError:
#     print("The value you have entered is out of Index please enter in b/w the index")
#
# except ValueError:
#     print("Please enter the valid value")
#
# print("Terminated gracefully")


#OR we can have exception handling message given automatically
try:
    print(L[index])

except (IndexError,ValueError) as msg:
    print(msg)

print("Terminated gracefully")
