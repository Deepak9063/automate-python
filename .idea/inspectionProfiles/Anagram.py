s1 = input("Enter the first String")
s2 = input("Enter the second String")

if len(s1) != len(s2):
    print("It is not a Anagram")

else:
    for i in s1:
        if i not in s2:
            print("It is not Anagram")

    else:
        print("It is Anagaram")



