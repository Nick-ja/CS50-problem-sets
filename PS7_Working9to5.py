import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # search for the correct format
    matches = re.search(r"^((?:[0-9]|1[0-2])(?::[0-5][0-9])?\s(?:AM|PM))\sto\s((?:[0-9]|1[0-2])(?::[0-5][0-9])?\s(?:AM|PM))$", s)
    if matches:
        # assign the start time to a variable
        start_time = convert_start_hour(matches.group(1))

        # assign the end time to a variable
        end_time = convert_end_hour(matches.group(2))

    else:
        # if there are no matches, raise a ValueError
        raise ValueError

    # return the correct answer
    return str(start_time) + " to " + end_time


def convert_start_hour(sh):
    # split the start hour and the AM/PM
    start_hour, start_hour_am_pm = sh.split(" ")

    try:
        # try to split the start hours and start minutes
        stripped_start_hour = start_hour.split(":")

        # assign the start hours
        stripped_hour = int(stripped_start_hour[0])

        # assign the start minutes
        stripped_minutes = stripped_start_hour[1]

    # if only used the hour and AM or PM
    except IndexError:
        # assign start hour
        stripped_hour = int(start_hour)

        # assign the 00 to get the full hour
        stripped_minutes = "00"

    # if the start time is in AM, add 12 hours to the time
    if start_hour_am_pm == "PM":
        # if the time is 12 PM it should output as 12:00 instead of 24:00
        if stripped_hour == 12:
            full_hour = stripped_hour
        else:
        # is the time is not 12 PM just add 12 to the AM time
            full_hour = stripped_hour + 12

    # if the start time is AM, and it's 12 hour => time should be converted to 0 hours
    if start_hour_am_pm == "AM" and stripped_hour == 12:
        full_hour = 0
    # if the start time is in AM and the time is less than 12 hours, just keep the same time
    if start_hour_am_pm == "AM" and stripped_hour < 12:
        full_hour = stripped_hour

    return f"{full_hour:02}:{stripped_minutes}"


def convert_end_hour(eh):
    # split the end hour and the AM/PM
    end_hour, end_hour_am_pm = eh.split(" ")

    try:
        # try to split the end hours and end minutes
        stripped_end_hour = end_hour.split(":")

        # assign the start hours
        stripped_hour = int(stripped_end_hour[0])

        # assign the start minutes
        stripped_minutes = stripped_end_hour[1]

    # if only used the hour and AM or PM
    except IndexError:
        # assign end hour
        stripped_hour = int(end_hour)

        # assign the 00 to get the full hour
        stripped_minutes = "00"

    # if the end time is in AM, add 12 hours to the time
    if end_hour_am_pm == "PM":
        # if the time is 12 PM it should output as 12:00 instead of 24:00
        if stripped_hour == 12:
            full_hour = stripped_hour
        else:
        # is the time is not 12 PM just add 12 to the AM time
            full_hour = stripped_hour + 12

    # if the end time is AM, and it's 12 hour => time should be converted to 0 hours
    if end_hour_am_pm == "AM" and stripped_hour == 12:
        full_hour = 0
    # if the end time is in AM and the time is less than 12 hours, just keep the same time
    if end_hour_am_pm == "AM" and stripped_hour < 12:
        full_hour = stripped_hour

    return f"{full_hour:02}:{stripped_minutes}"


if __name__ == "__main__":
    main()
