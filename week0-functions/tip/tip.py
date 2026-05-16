"""
tip.py - Tip Calculator.

This module implements a solution for the "Tip" problem of the CS50,
which calculates the tip a customer should leave according to the cost of the
meal and the percentage he/she would pay.

Author:
    Daniel Casasola Guerrero <danicg06>

Example:
    >>> python tip.py

    ----------------
     TIP CALCULATOR
    ----------------

    Cost of the meal:  $40.00
    Percentage to tip: 50%
    -> The tip is: $20.00
"""

# ============================================================================
# CONSTANTS
# ============================================================================

HEADER = """
----------------
 TIP CALCULATOR
----------------
"""

PROMPT1 = "Cost of the meal: "

PROMPT2 = "Percentage to tip: "

PREOUTPUT = "-> The tip is: $"

# ============================================================================
# FUNCTIONS
# ============================================================================
def print_header():
    """
Prints the corresponding header, declared right above as a constant string.
"""
    print(HEADER)


def dollars_to_float(d):
    """
Receives a parameter formatted as '$##.##' (# is a decimal digit) and returns
the amount as a float, removing the $.

Parameter:
d - string with the format '$##.##'.

Return value:
output - float from d, removing the $ sign.
"""

    # If the parameter starts with "$", then it should be removed.
    #
    # removeprefix("abc"): if the string starts with "abc", it is removed.
    if d.startswith("$"):
        d = d.removeprefix("$")
        # d.lstrip("$") ANOTHER ALTERNATIVE
        # lstrip("abc"): removes all the leading specified characters from
        #                the string. The string "abc" is seen as the characters
        #                on its own, removing all combinations of them.
    output = float(d)

    return output


def percent_to_float(p):
    """
Receives a parameter formatted as '##%' (# is a decimal digit) and returns
the percentage as a float, removing the % and dividing that by 100.

Parameter:
p - string with the format '##%'.

Return value:
output - corresponding float of the parameter p.
"""
    # If the parameter ends with % then it should be removed.
    #
    # removesuffix("abc"): if the string ends with "abc", it is removed.
    if p.endswith("%"):
        p = p.removesuffix("%")
        # p.rstrip("%") ANOTHER ALTERNATIVE
        # rstrip("abc"): removes all the trailling specified characters from
        #                the string. The string "abc" is seen as the characters
        #                on its own, removing all combinations of them.

    # converts the resulting percentage into the corresponding float.
    output = float(p)
    output = output/100

    return output


# ============================================================================
# MAIN
# ============================================================================
def main():

    # Print header
    print_header()

    # INPUTS
    dollars = dollars_to_float(input(PROMPT1))
    percent = percent_to_float(input(PROMPT2))

    # calculates the corresponding tip (given percentage of the meal cost)
    tip = dollars * percent

    # OUTPUT
    print(f"{PREOUTPUT}{tip:.2f}")

main()
