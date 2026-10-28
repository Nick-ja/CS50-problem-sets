user_input = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

corrected_input = user_input.strip().lower()

if corrected_input == "42" or corrected_input == "forty-two" or corrected_input == "forty two" or corrected_input == "Forty Two" or corrected_input == "Forty-Two":
    print("Yes")
else:
    print("No")
