import sys
import csv


def main():
    files = command_line_arguments()
    before_file = opening_file(files[0])
    after_file = split_name(before_file)

    with open(sys.argv[2], "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in after_file:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})


def command_line_arguments():
    #  implement a program that expects exactly two command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    # If the user does not specify exactly two command-line argument
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # or if the specified files name does not end in .csv
    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")
    # if there are 2 arguments given, return the file names
    if len(sys.argv) == 3:
        return sys.argv[1:]


def opening_file(file):
    before = []
    # opening the before file
    try:
        with open(file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                before.append({"name": row["name"], "house": row["house"]})
    # if the specified file does not exist, the program should instead exit via sys.exit
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    return before


def split_name(before_file):
    after_file = []

    for row in before_file:
        name = row["name"]
        house = row["house"]
        separated_names = name.split(",")
        after_file.append({"last": separated_names[0], "first": separated_names[1].lstrip(), "house": house})
    return after_file


if __name__ == "__main__":
    main()
