"""
camel.py - Camel case to snake case.

This module implements a solution for the "camelCase" problem of CS50, which
prompts the user for a name of a variable in camelCase and converts the
corresponding name to snake case.
It should be assumed that the user's input is in camel case.

Author:
    Daniel Casasola Guerrero <danicg06>

Example:
    >>> python camel.py

    ---------------------
     CAMEL TO SNAKE CASE
    ---------------------

    camelCase: myNameIsPepe
    snake_case: my_name_is_pepe
"""

# ============================================================================
# CONSTANTS
# ============================================================================

HEADER = """
---------------------
 CAMEL TO SNAKE CASE
---------------------
"""

PROMPT = "camelCase: "

PREOUTPUT = "snake_case: "

SNAKE_CASE_SEP = "_"


# ============================================================================
# FUNCTIONS
# ============================================================================
def print_header():
    """
Prints the corresponding header, declared right above as a constant string.
"""
    print(HEADER)


def convert_case(variable):
    """
Converts the received name of a variable, assumed to be in camel case, into
snake case.

Parameters:
variable - string of the corresponding name of the variable in camel case.

Return value:
output - string of the corresponding name of the variable in snake case.
"""
   # removes the leading and trailing whitespaces from the variable's name.
    variable = variable.strip()

    # converted string must be initialized in order to be concatenated.
    output = ""

    # iterates over each of the characters of the string in order to find the
    # letters in uppercase.
    for char in variable:
        # if the iterated characted is uppercase, then, it is concatenated to
        # the output string: "_" + "character" in lowercase.
        # Otherwise, the character is just concatenated to the string.
        if char.isupper():
            output += SNAKE_CASE_SEP + char.lower()
        else:
            output += char

    return output

# ============================================================================
# MAIN
# ============================================================================
def main():

    # Print header
    print_header()

    # INPUT
    variable = input(PROMPT)

    # converts the user's input into snake case.
    output = convert_case(variable)

    # OUTPUT
    print(f"{PREOUTPUT}{output}")

if __name__ == "__main__":
    main()

