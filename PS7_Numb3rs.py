import re


def main():
    print(validate(input("IPv4 Address: ").strip()), end="")


def validate(ip):
    matches = re.search(r"^([0-9][0-9]?|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9][0-9]?|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9][0-9]?|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9][0-9]?|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$", ip)
    if matches:
        return True
    else:
        return False


if __name__ == "__main__":
    main()




