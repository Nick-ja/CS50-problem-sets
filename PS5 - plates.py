# Remove "PS5 -" from this file and PS5 - test_plates.py file
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # length check / first 2 letters check / all letters or numbers check
    if 2 <= len(s) <= 6 and s[0:2].isalpha() and s.isalnum():
        # start to loop over every character
        for character in s:
            # if the current character is a number
            if character.isdigit():
                # determine the place of the number in the string
                index = s.index(character)
                # if no letters after the first digit and the first number is not 0
                if s[index:].isdigit() and character != "0":
                    # return "valid"
                    return True
                else:
                    # return "invalid"
                    return False
        return True
    return False


if __name__ == "__main__":
    main()
