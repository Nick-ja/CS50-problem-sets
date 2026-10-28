from validator_collection import validators, errors


def main():
    print(check_email(input("What's your email address? ")))


def check_email(email):
    try:
        email_address = validators.email(email, allow_empty = False)
        return "Valid"
    except errors.InvalidEmailError:
        return "Invalid"


if __name__ == "__main__":
    main()
