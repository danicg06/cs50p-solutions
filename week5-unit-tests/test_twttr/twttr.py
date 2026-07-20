"""
twttr.py - Omitting vowels.

This module implements a solution for the "Just setting up my twttr" problem of
CS50, which asks the user for a text and converts the text by omitting the
corresponding vowels.

Author:
    Daniel Casasola Guerrero <danicg06>

Example:
    >>> python twttr.py

    -----------------
     OMITTING VOWELS
    -----------------

    Input: HelloMyFriend
    Output: HllMyFrnd
"""

# ============================================================================
# CONSTANTS
# ============================================================================

HEADER = """
-----------------
 OMITTING VOWELS
-----------------
"""

PROMPT = "Input: "

PREOUTPUT = "Output: "

VOWELS = "aeiou"

# ============================================================================
# FUNCTIONS
# ============================================================================
def print_header():
    """
Prints the corresponding header, declared right above as a constant string.
"""
    print(HEADER)


def shorten(text):
    """
Converts the parameter text by omitting its vowels.

Parameters:
text - string of the text to convert.

Return value:
output - string of the corresponding no-vowels text.
"""

    # removes the leading and trailing whitespaces from the text.
    text = text.strip()

    # converted string must be initialized in order to be concatenated.
    output = ""

    # iterates over each of the characters of the string in order to find its
    # vowels.
    for char in text:
        # if the iterated characted, in lowercase, is not a vowel, then, it is
        # concatenated to the output string.
        # Otherwise, it is not taken into account.
        if char.lower() not in VOWELS:
            output += char

    return output

# ============================================================================
# MAIN
# ============================================================================
def main():

    # Print header
    print_header()

    # INPUT
    text = input(PROMPT)

    # converts the user's input into snake case.
    output = shorten(text)

    # OUTPUT
    print(f"{PREOUTPUT}{output}")

if __name__ == "__main__":
    main()

