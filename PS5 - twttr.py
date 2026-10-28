# Remove "PS5 -" from this file and test_twttr.py file
def main():
    # get user input
    string = input("Input: ")
    # print out result
    print(shorten(string))


def shorten(word):
    # create a wordlist
    wordlist = []

    # iterate over every letter in word
    for letter in word:
        # check that letter is not a lowercase vowel
        if not letter.lower() in ["a", "e", "i", "o", "u"]:
            # add the letter to the wordlist
            wordlist.append(letter)

    # return a string from the wordlist
    return "".join(wordlist)


if __name__ == "__main__":
    main()
