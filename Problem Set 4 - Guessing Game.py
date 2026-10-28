import random

# Prompts the user for a level, n. If the user does not input a positive integer, the program should prompt again
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

# Randomly generates an integer between 1 and n, inclusive, using the random module.
correct_guess = random.randint(1, level)

# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
while True:
    try:
        guess = int(input("Guess: "))
        if guess < 0:
            continue
        # If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
        if guess < correct_guess:
            print("Too small!")
        # If the guess is larger than that integer, the program should output Too large! and prompt the user again.
        elif guess > correct_guess:
            print("Too large!")
        # If the guess is the same as that integer, the program should output Just right! and exit.
        elif guess == correct_guess:
            print("Just right!")
            break
    except ValueError:
        pass










































