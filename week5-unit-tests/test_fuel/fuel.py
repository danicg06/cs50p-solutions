"""
fuel.py - Fuel Gauge.

This module implements a solution for the "Fuel Gauge" problem of CS50, which
prompts the user for a fraction, formatted as X/Y (X and Y integers). Then,
it outputs how much fuel is in the tank as a percentage, rounded to the nearest
integer. If 1% or less remains, it outputs E (empty); else, if 99% or more
remains, it outputs F (full).
The main aim of this module is to prompt the user again if the input is not a
valid fraction, such as X and Y not being integers, X being greater than Y or Y
being 0.

Author:
    Daniel Casasola Guerrero <danicg06>

Example:
    >>> python fuel.py

    ------------
     FUEL GAUGE
    ------------

    Fraction: 1/3
    33%

"""

# ============================================================================
# CONSTANTS
# ============================================================================

HEADER = """
------------
 FUEL GAUGE
------------
"""

PROMPT = "Fraction: "


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

def convert(fraction):
    """
    Returns the rounded fraction of the received string formatted as X/Y.

    If it is a division by zero or X > Y or one of them is not an integer,
    then the corresponding error is returned.

    Arguments:
    fraction - string formatted as X/Y

    Return value:
    The corresponding and rounded percentage.
    """

    # removes the leading and trailing whitespaces from the input.
    fraction = fraction.strip()

    # makes a list of two elements: the dividend and divisor.
    X, Y = fraction.split("/")

    X = int(X)
    Y = int(Y)

    if (Y == 0):
        raise ZeroDivisionError
    elif X > Y or (X/Y < 0):
        raise ValueError
    else:
        return round((X/Y)*100)

def gauge(percentage):
    """
    Outputs "E" if 1% or less of fuel remains, or "F" if 99% or more of fuel remains
    in the tank.

    Arguments:
    percentage - percentage calculated from the input fraction.

    Return value:
    output - string of the corresponding fuel percentage remaining.
    """

    if percentage <= 1: # empty tank
        output = "E"
    elif percentage >= 99: # full tank
        output = "F"
    else:
        output = f"{percentage}%"

    return output


# ============================================================================
# MAIN
# ============================================================================
def main():

    # Print header
    print_header(HEADER)

    # INPUT of the corresponding fraction
    fraction = input(PROMPT)

    # Converts the fraction in a percentage
    percentage = convert(fraction)

    # Returns the correct string corresponding to the percentage
    output = gauge(PROMPT)

    # OUTPUT
    print(f"{output}")

if __name__ == "__main__":
    main()

