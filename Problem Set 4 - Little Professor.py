import random


def main():
    chosen_level = get_level()
    score = 0
    tries = 1
    i = 1
    while i <= 10:
        generated_integers = generate_integer(chosen_level)
        x = generated_integers[0]
        y = generated_integers[1]
        z = generated_integers[2]
        answer = int(input(f"{x} + {y} = "))
        if answer == z:
            i += 1
            score += 1
        else:
            tries += 1
            while tries < 4:
                print("EEE")
                answer = int(input(f"{x} + {y} = "))
                if answer == z:
                    i += 1
                    break
                elif tries == 3:
                    print("EEE")
                    print(f"{x} + {y} = {z}")
                    i += 1
                    tries = 1
                    break
                else:
                    tries += 1
    print(f"Score: {score}")


# wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3
def get_level():
    # Prompts the user for a level,n. If the user does not input 1, 2, or 3, the program should prompt again.
    while True:
        try:
            wanted_level = int(input("Level: "))
            if 0 < wanted_level < 4:
                return wanted_level
        except ValueError:
            pass


# generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:
def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        z = x + y
        return x, y, z
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
        z = x + y
        return x, y, z
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
        z = x + y
        return x, y, z


if __name__ == "__main__":
    main()





































