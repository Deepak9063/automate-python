# s  = "Have a good day"
#
# rev_sen = []
#
# sen_split = s.split(" ")
#
# for i in range(len(sen_split)-1,-1,-1):
#
#     if i==2:
#         second_word_rev = ""
#         word = sen_split[i]
#         for i in range(len(word)-1,-1,-1):
#             second_word_rev += word[i]
#         rev_sen.append(second_word_rev)
#
#     else:
#         rev_sen.append(sen_split[i])
#
#
# print(second_word_rev)
#
# print(rev_sen)


#reverse sentence
s = "My name is Deepak"
s1 = []
sen_split = s.split(" ")

for i in range(len(sen_split)-1,-1,-1):
    if i==3:
        third_word = ""
        word = sen_split[i]
        for i in range(len(word)-1,-1,-1):
            third_word += word[i]

        s1.append(third_word)
        print(third_word)

    else:
        s1.append(sen_split[i])

print(s1)


















