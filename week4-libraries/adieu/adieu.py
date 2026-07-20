"""
adieu.py - Adieu, Adieu.

This module implements a solution for the "Adieu" problem of CS50, which prompts
the user for a name, one per line, until it inputs control-d. The names will be
separated by commas and an 'and' correctly.

Author:
    Daniel Casasola Guerrero <danicg06>

Example:
    >>> python adieu.py

    -------------
     ADIEU ADIEU
    -------------

    Name: Daniel
    Name: Peter
    Name: Juan
    Name:
    Adieu, adieu to Daniel, Peter and Juan

"""

# ============================================================================
# CONSTANTS
# ============================================================================

HEADER = """
-------------
 ADIEU ADIEU
-------------
"""

PROMPT = "Name: "

PREOUTPUT = "Adieu, adieu, to "

# ============================================================================
# LIBRARIES
# ============================================================================
from inflect import engine
# ============================================================================
# FUNCTIONS
# ============================================================================
def print_header(header):
    """
    Prints the corresponding header.

    Arguments:
        header - string of the header to be printed.
    """
    print(header)


def get_names(PROMPT):
    """
    Prompts the user for names, one per line, until it inputs control-d.
    Then return "Adieu, adieu to name1, name2, ... and nameN".

    Arguments:
        PROMPT - global constant string of the corresponding prompt.

    Return value:
        output - string of the corresponding converted text.
    """

    people = []
    while True:
        try:
            name = input(PROMPT)

            people.append(name)
        except EOFError:
            print("\n")
            break

    p = engine()
    return  p.join(people)


# ============================================================================
# MAIN
# ============================================================================
def main():

    # Print header
    print_header(HEADER)

    # INPUT the user for a text
    # Returns the text with the font changed
    output = get_names(PROMPT)

    print(f"{PREOUTPUT}{output}")

if __name__ == "__main__":
    main()

