def main():
    camel_case = input("camelCase: ")
    snake_case(camel_case)


def snake_case(x):
    word_list = []

    for letter in x:
        if letter.isupper():
            word_list += "_" + letter
        else:
            word_list += letter

    for i in word_list:
        print(i.lower(), end="")


main()
