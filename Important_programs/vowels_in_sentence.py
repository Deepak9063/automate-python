sentence = input("Please enter the string")
vowels_sentence= ""

vowels = "aeiouAEIOU"

for char in sentence:
    if char in vowels:
        vowels_sentence += char

print(vowels_sentence)



