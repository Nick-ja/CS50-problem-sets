def main():
    fraction = convert(input("Fraction: "))
    print(gauge(fraction))


def convert(fraction):
    while True:
        try:
            # convert expects a str in X/Y format as input
            x, y = fraction.split("/")
            # wherein each of X and Y is an integer
            x, y = int(x), int(y)
            # divide x by y
            result = x / y
            # if x is smaller than y return output
            if x <= y:
                # return the fraction as a percentage rounded to the nearest int between 0 and 100, inclusive.
                return round(result * 100)
            # if x is greater than y re-prompt
            else:
                fraction = input("Fraction: ")
                pass
        # raise the errors
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    # percentage lower or equal to 1 should output E
    if percentage <= 1:
        return "E"
    # percentage higher or equal to 99 should output F
    elif percentage >= 99:
        return "F"
    # otherwise output percentage as Z%
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
