s = input("Enter a String")

# Here we // symbol for the purpose of floor division so that we will not get the floating values

first_half = s[:len(s)//2:]

secondhalf_reverse = s[len(s)-1:(len(s)//2)-1:-1] #since ending point is exclusive so we have to to substact on from it

print(first_half+secondhalf_reverse)