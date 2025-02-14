num = int(input("Please enter the Number to reverse"))

original_num = num

digit =0
rev=0
while num>0:
    digit = num%10
    rev = rev*10+digit
    num = num//10

print(rev)

if rev == original_num:
    print("It is a palindrome")
else:
    print("It is not a palindrome")