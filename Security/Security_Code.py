#!/usr/bin/env python3
"""
Security_Code Version 1
Python 3.7
"""

import datetime
import os.path
import random
import string


def check_file():
    """Check if file exists."""
    if os.path.exists("transfer.txt"):
        return

    else:
        with open("transfer.txt", "w+") as file:
            return


def expiration():
    """
    Set next day expiration date and generate a random, 2 letter
    security code that changes daily to indicate expiration.
    """
    # Sets letters to uppercase.
    letters = string.ascii_uppercase

    # Gets date and time.
    date = datetime.datetime.now()

    # Extracts time of day and adds 3 hours.
    future_time = date + datetime.timedelta(0, 10800)
    new_time = list(str(future_time))
    del new_time[0:11]
    del new_time[4:14]
    new_time = "".join(new_time)

    # Sets date format and adds a day.
    expires = f"{date.year}-0{date.month}-0{date.day + 1}"

    # Removes time from date.
    list_date = list(str(date))
    del list_date[10:26]
    new_date = "".join(list_date)

    with open("transfer.txt", "r+") as file:
        current_data = file.readlines()

    if current_data == ["\n"] or []:
        with open("transfer.txt", "w") as file:
            file.write(f'Expires: {expires}\n{"XX"}\n{new_time}')

    else:
        pass

    if new_date == expires:
        with open("transfer.txt", "w") as file:
            code_1 = random.choice(letters)
            code_2 = random.choice(letters)
            day_code = f"{code_1}{code_2}"
            file.write(f"""Expires: {day_code}\n{expires}\n{new_time}""")

    else:
        raise SystemExit


if __name__ == "__main__":
    check_file()
    expiration()
