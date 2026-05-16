"""
meal.py - Hour to meal.

This module implements a solution for the "Meal Time" problem of the
CS50, which prompts the user for a time formatted as (#)#:##, being # a decimal
digit, and returns the corresponding meal:

7:00 - 8:00   -> breakfast
12:00 - 13:00 -> lunch
18:00 - 19:00 -> dinner

If the input is not a time for a meal, it indicates it to the user.
Moreover, if the input is not a possible time, such as, -4:35 or 43:66, the
output is the same.
Also, it will be assumed that each meal's time range is inclusive.

Author:
    Daniel Casasola Guerrero <danicg06>

Example:
    >>> python meal.py

    -----------
     MEAL TIME
    -----------

    Time: 12:00
    -> lunch time
"""

# ============================================================================
# CONSTANTS
# ============================================================================

HEADER = """
------------
 CALCULATOR
------------
"""

PROMPT = ("Expression: ")

NO_MEAL_TIME = "It's not meal time 🙁"

NO_REAL_TIME = "That's not a possible time."

BREAKFAST_TIME = "breakfast time"

LUNCH_TIME = "lunch time"

DINNER_TIME = "dinner time"


# ============================================================================
# FUNCTIONS
# ============================================================================
def print_header():
    """
Prints the corresponding header, declared right above as a constant string.
"""
    print(HEADER)


def convert(time):
    """
Converts the received time to the corresponding numer of hours as a float.
The time format must be (#)#:##, where # is a decimal digit.

Parameters:
time - string of the corresponding time formatted as (#)#:##

Return value:
output - float value that refers to the corresponding hours of the given time.
"""
    # splits the string expression into two strings, one for the hours and the
    # other for the minutes.
    hours, minutes = time.split(":")
    hours   = int(hours)
    minutes = int(minutes)

    # as we want to calculate the corresponding hours, the number of hours
    # remain the same, whereas the minutes have to be converted.
    # The precise conversion is the following:
    # converted_minutes = minutes/60, as an hour has 60 minutes.
    output = float(hours + minutes/60)

    return output

def is_real_time(time):
    """
Receives a time (formatted as (#)#:##) and indicates if it a real time.

Parameters:
time - string of the corresponding time formatted as (#)#:##

Return value:
output - true if the given time is possible, false if not.
"""
    # splits the string expression into two strings, one for the hours and the
    # other for the minutes.
    hours, minutes = time.split(":")
    hours   = int(hours)
    minutes = int(minutes)

    return (0 <= hours and hours <= 23 and 0 <= minutes and minutes <= 59)


def meal_time(time):
    """
Depending on the received time (formatted as (#)#:##), indicates the user which
meal time it is.
If the input is not a time for a meal, it indicates it to the user.
Moreover, if the input is not a posibble time, such as, -4:35 or 43:66, the
output is the same.
Also, it will be assumed that each meal's time range is inclusive.

Parameters:
time - string of the corresponding time formatted as (#)#:##

Return value:
output - float value that refers to the corresponding hours of the given time.
"""
    # removes the leading and trailing whitespaces from the parameter file.
    time = time.strip()

    # checks if the input time is a real and possible time.
    if is_real_time(time):
        output = float(convert(time))

        if (7 <= output and output <= 8):
            output = BREAKFAST_TIME
        elif (12 <= output and output <= 13):
            output = LUNCH_TIME
        elif (18 <= output and output <= 19):
            output = DINNER_TIME
        else:
            output = NO_MEAL_TIME
    else:
        output = NO_REAL_TIME

    return output


# ============================================================================
# MAIN
# ============================================================================
def main():

    # Print header
    print_header()

    # INPUT
    time = input(PROMPT)

    # indicates the user the corresponding meal time.
    output = meal_time(time)

    # OUTPUT
    print(f"{output}")

if __name__ == "__main__":
    main()

