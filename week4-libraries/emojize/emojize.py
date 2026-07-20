"""
emojize.py - Text to Emoji.

This module implements a solution for the "Emojize" problem of CS50,
which prompts the user for a string text formatted as :[text]: and converts it
into an emoji.

Author:
    Daniel Casasola Guerrero <danicg06>

Example:
    >>> python emojize.py

    ---------------
     TEXT TO EMOJI
    ---------------

    Input: :thumbsup:
    Emoji: 👍

"""

# ============================================================================
# CONSTANTS
# ============================================================================

HEADER = """
---------------
 TEXT TO EMOJI
---------------
"""

PROMPT = "Input: "

PREOUTPUT = "Emoji: "

# ============================================================================
# LIBRARIES
# ============================================================================
from emoji import emojize  # emojize

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

def get_emojize(PROMPT):
    """
    Prompts the user for a text to get "emojized".

    Arguments:
        PROMPT - global constant string of the corresponding prompt.

    Return value:
        output - string of the corresponding emojized text.
    """

    text = input(PROMPT)

    return emojize(text, language = 'alias')


# ============================================================================
# MAIN
# ============================================================================
def main():

    # Print header
    print_header(HEADER)

    # INPUT the user for a text
    # Returns the emojized text
    output = get_emojize(PROMPT)

    print(f"{PREOUTPUT}{output}")

if __name__ == "__main__":
    main()

