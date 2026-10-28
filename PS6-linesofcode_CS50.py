import sys


def main():
    # check the command line arguments
    command_line_arguments()
    # open the file
    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
    # or if the specified file does not exist the program should instead exit via sys.exit.
    except FileNotFoundError:
        sys.exit("File does not exist")

    # setting the counter to 0
    coded_lines = 0
    # starting the loop through the lines
    for line in lines:
        # check for # or empty line in the file (per line)
        if check_lines(line):
            coded_lines += 1
    # print the amount of lines with code
    print(coded_lines)


def command_line_arguments():
    #  implement a program that expects exactly one command-line argument
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    # If the user does not specify exactly one command-line argument
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # or if the specified file’s name does not end in .py
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")


def check_lines(line):
    # if the line is empty, return False
    if line.isspace():
        return False
    # if the line starts with a #, return False
    if line.lstrip().startswith("#"):
        return False
    # otherwise (row with code), return True
    return True


if __name__ == "__main__":
    main()
