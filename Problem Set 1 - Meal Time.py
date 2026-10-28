def main():
    time = input("What time is it? ")
    convert(time)

    if 7.0 <= convert(time) <= 8.0:
        print("breakfast time")
    elif 12.0 <= convert(time) <= 13.0:
        print("lunch time")
    elif 18.0 <= convert(time) <= 19.0:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    converted_hours = int(hours)
    converted_minutes = float(round(int(minutes) / 60, 2))
    x = converted_hours + converted_minutes
    return x


if __name__ == "__main__":
    main()
