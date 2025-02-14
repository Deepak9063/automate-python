# To check weather the String is Palindrome or not

s = input("Enter a String\n")

if s==s[::-1]:
    print(s,"It is a Palindrome")
else:
    print(s,"It is not a palindrome")


# Reverse Each word in a Sentence
#     words = s.split()
#
#     Reversed_sentence = words[::-1]
#
#     word_reverse = ' '.join(Reversed_sentence)
#
#     print(word_reverse)

sentence = input("Please enter the sentence");

rev_sentence = sentence.split(" ")[::-1]

print(' '.join(rev_sentence))