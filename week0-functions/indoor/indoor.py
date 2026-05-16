"""
indoor.py - Text to lowercase converter (referred to indoor voice).

This module implements a solution for the "indoor" problem of the CS50,
which converts to lowercase an input requested to the user, returning it
in lowercase. Whitespaces and punctuation should not be changed.

Author:
    Daniel Casasola Guerrero <danicg06>

Example:
    >>> python indoor.py

    -----------------------------
     TEXT TO LOWERCASE CONVERTER
    -----------------------------

    Text: HapPy bIrthdAy
      ->  happy birthday
"""

# ============================================================================
# CONSTANTS
# ============================================================================

HEADER = """
-----------------------------
 TEXT TO LOWERCASE CONVERTER
-----------------------------
"""

PROMPT    = "Text: "

PREOUTPUT = "  ->  "


# ============================================================================
# FUNCTIONS
# ============================================================================
def print_header():
    """
Prints the corresponding header, declared right above as a constant string.
"""
    print(HEADER)


# ============================================================================
# MAIN
# ============================================================================
def main():

    # Print header
    print_header()

    # INPUT
    text = input(PROMPT)

    # lowercase the text
    output = text.lower()

    # OUTPUT
    print(f"{PREOUTPUT}{output}")

main()
