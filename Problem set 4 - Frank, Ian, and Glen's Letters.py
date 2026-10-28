import sys
import random
from pyfiglet import Figlet


def main():
    figlet = Figlet()
    available_fonts = figlet.getFonts()

    if sys.argv[1] == "-f" or sys.argv[1] == "--font":

        if sys.argv[2] in available_fonts:

            desired_text = str(input("Input: "))

            if len(sys.argv) < 2:
                random_font(figlet, available_fonts, desired_text)

            elif len(sys.argv) > 2:
                desired_font = sys.argv[2]
                print(desired_font)
                custom_font(figlet, desired_font, desired_text)
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")


def random_font(figlet, af, s):
    figlet.setFont(font=random.choice(af))
    print(figlet.renderText(s))


def custom_font(figlet, f, s):
    figlet.setFont(font=f)
    print(figlet.renderText(s))


if __name__ == "__main__":
    main()