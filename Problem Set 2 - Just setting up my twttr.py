string = input("Input: ")
vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
word_list = []

for letter in string:
    if letter in vowels:
        continue
    else:
        word_list += letter

for l in word_list:
    print(l, end="")
