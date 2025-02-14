# sentence = input("Please enter the sentence to reverse")
# sentence_split = sentence.split(" ")[::-1]
# rev_sentence = " ".join(sentence_split)
#
# print(rev_sentence)

sentence = input("Enter the string")
rev_sentence = ""
sentence_split = sentence.split(" ")

for i in range(len(sentence_split)-1,-1,-1):
    rev_sentence += sentence_split[i]

print(rev_sentence)

















