import operator
import inflect
from datetime import date
import sys


def main():
    # prompt user for date of birth in YYYY-MM-DD
    entered_birth_date = input("Date of Birth: ").strip()

    # convert date to date data
    birth_date = get_birth_date(entered_birth_date)

    # get today's date
    today_date = date.today()

    # calculate difference in days
    difference_in_days = calculate_difference(birth_date, today_date)

    # calculate difference in minutes
    difference_in_minutes = convert_days_to_minutes(difference_in_days)

    # convert the minutes into words without and word
    word_minutes = convert_minutes_to_string(difference_in_minutes)

    # print out the result
    print(word_minutes + " minutes")


def get_birth_date(birth_date):
    # try to convert birthdate to date data
    try:
        # convert string to a date
        return date.fromisoformat(birth_date)
    except ValueError:
        # exit the program is no valid date is given
        sys.exit("Invalid date")


def calculate_difference(berth, today):
    # calculate difference between today and the birthdate in days
    difference = operator.sub(today, berth)
    return difference.days


# print how old they are in minutes, rounded to the nearest integer
def convert_days_to_minutes(did):
    # calculate hours by multiplying difference in days by 24
    hours = did * 24
    # calculate minutes by multiplying hours by 60
    minutes = hours * 60
    # return the minutes
    return minutes


# convert to English words instead of numerals
def convert_minutes_to_string(minutes):
    p = inflect.engine()
    # without "and" between words as parameter
    words = p.number_to_words(minutes, andword="")
    return words.capitalize()


if __name__ == "__main__":
    main()
