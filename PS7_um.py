import re


def main():
    print(count(input("Text: ")))


def count(s):
    amount_matches = 0
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    for match in matches:
        amount_matches += 1
    return amount_matches


if __name__ == "__main__":
    main()
