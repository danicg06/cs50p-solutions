"""
outdated.py - Anno Domini to YYYY-MM-DD.

This module implements a solution for the "Outdated" problem of CS50, which
prompts the user for a date formatted like M/D/YYYY or Month Day, Year.
Then, outputs the corresponding date formatted as YYYY-MM-DD.
If the user's input is not a valid date, prompt the user again.

Author:
    Daniel Casasola Guerrero <danicg06>

Example:
    >>> python outdated.py

    ----------------
     DATE CONVERTER
    ----------------

    Date: 10/5/1837
    1837-10-05

    Date: January 4, 2006
    2006-01-04
"""

# ============================================================================
# CONSTANTS
# ============================================================================

HEADER = """
----------------
 DATE CONVERTER
----------------
"""

PROMPT = "Date: "

MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# ============================================================================
# FUNCTIONS
# ============================================================================
def print_header(header):
    """
    Prints the corresponding header.

    Arguments:
        HEADER - string of the header to be printed.
    """
    print(header)

def get_date():
    """
    Prompts the user for a date formatted like M/D/YYYY or Month Day, Year.
    Then, outputs the corresponding date formatted as YYYY-MM-DD.
    If the user's input is not a valid date, prompt the user again.

    Return value:
        output - string with the corresponding date.
    """

    # builds the dict
    d = dict()
    i = 0
    for month in MONTHS:
        i += 1
        d[MONTHS[i-1]] = i

    # prompts the user until a valid date is entered.
    while True:
        try:
            date = input(PROMPT)

            # removes the leading and trailing whitespaces from the date.
            date = date.strip()

            # if the date is formatted as Month Day, Year.
            if len(date.split(" ")) == 3 and date.count(",") == 1:
                date_list = date.split(" ")

                # variable of the date's year.
                year = int(date_list[2])

                # if the year is valid.
                if year >= 0:
                    # variable of the date's month.
                    month = int(d[date_list[0]])

                    # if the month is valid.
                    if month >= 1 and month <= 12:

                        # if the comma is in the right place.
                        if (date_list[1][-1] == ","):
                            # variable of the date's day, removing the comma.
                            day = int(date_list[1][:-1])

                            # if the day is valid.
                            if day >= 1 and day <= 31:

                                # the date is valid and it is converted.
                                output = f"{year:04}-{month:02}-{day:02}"
                                return output
            # if the date is formatted as M/D/YEAR.
            elif len(date.split("/")) == 3:
                date_list = date.split("/")

                # variable of the date's year
                year = int(date_list[2])

                # if the year is valid.
                if year >= 0:

                    # variable of the date's month.
                    month = int(date_list[0])

                    # if the month is valid.
                    if month >= 1 and month <= 12:

                        # variable of the date's day.
                        day = int(date_list[1])

                        # if the day is valid.
                        if day <= 31 and day >= 1:

                            # the date is valid and it is converted.
                            output = f"{year:04}-{month:02}-{day:02}"
                            return output
        except (ValueError, KeyError):
            pass


# ============================================================================
# MAIN
# ============================================================================
def main():

    # Print header
    print_header(HEADER)

    # INPUT until the user enters a valid date.
    # returns the date formatted as YYYY-MM-DD.
    output = get_date()

    # OUTPUT
    print(f"{output}")

if __name__ == "__main__":
    main()

