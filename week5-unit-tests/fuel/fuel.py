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

    Fraction: p/q
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

def get_fuel(PROMPT):
    """
    Prompts the user until a valid fraction is entered and then calculates the
    corresponding percentage of fuel remaining in the tank.
    Outputs "E" if 1% or less of fuel remains, or "F" if 99% or more of fuel remains
    in the tank.

    Arguments:
    PROMPT - global constant string of the corresponding prompt.

    Return value:
    output - string of the corresponding fuel percentage remaining.
    """

    # prompts the user until a valid fraction is entered.
    while True:
        try:
            fraction = input(PROMPT)

            # removes the leading and trailing whitespaces from the input.
            fraction = fraction.strip()

            # makes a list of two elements: the dividend and divisor.
            X, Y = fraction.split("/")

            X = int(X)
            Y = int(Y)

            neg_fraction = (X/Y < 0)
            # if X > Y or the fraction is negative, then prompt the user again.
            if X <= Y and not neg_fraction:
                # calculates the fuel percentage.
                fuel = round((X/Y)*100)

                if fuel <= 1: # empty tank
                    output = "E"
                elif fuel >= 99: # full tank
                    output = "F"
                else:
                    output = f"{fuel}%"

                return output

        except (ValueError, ZeroDivisionError):
            pass


# ============================================================================
# MAIN
# ============================================================================
def main():

    # Print header
    print_header(HEADER)

    # INPUT and calculates the corresponding fuel
    output = get_fuel(PROMPT)

    # OUTPUT
    print(f"{output}")

if __name__ == "__main__":
    main()

