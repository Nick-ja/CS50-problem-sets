import sys
import csv
from tabulate import tabulate


def main():
    # check the command line arguments
    if command_line_arguments():
        file = sys.argv[1]

    # create the table list
    table = []
    # open the file
    with open(file) as file:
        reader = csv.DictReader(file, fieldnames=["Sicilian Pizza", "Small", "Large"])
        for row in reader:
            table.append({"Sicilian Pizza": row["Sicilian Pizza"], "Small": row["Small"], "Large": row["Large"]})
    # print out the table formatted as a grid
    print(tabulate(table[1:], headers=table[0], tablefmt="grid"))


def command_line_arguments():
    try:
        #  implement a program that expects exactly one command-line argument
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        # If the user does not specify exactly one command-line argument
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        # or if the specified file’s name does not end in .py
        if not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
        if len(sys.argv) == 2:
            return True, sys.argv[1]
    # if the specified file does not exist, the program should instead exit via sys.exit
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
