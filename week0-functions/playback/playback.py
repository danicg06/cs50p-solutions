"""
playback.py - Text to playback speed.

This module implements a solution for the "playback" problem of the CS50,
which slows a text requested to the user by replacing the spaces with three
periods.

Author:
    Daniel Casasola Guerrero <danicg06>

Example:
    >>> python playback.py

    ------------------------
     TEXT TO PLAYBACK SPEED
    ------------------------

    Text: I wish I had
      ->  I...wish...I...had
"""

# ============================================================================
# CONSTANTS
# ============================================================================

HEADER = """
------------------------
 TEXT TO PLAYBACK SPEED
------------------------
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

def playback(text):
    """
Slows the text received as a parameter by replacing the whitespaces with three
periods.
It must be secured that consecutive whitespaces are considered as an
unit. Also, it removes the leading and trailling whitespaces of the string.

Parameters:
text - string to convert.

Return value:
output - string received as a parameter but with the expected changes.

"""

    # We make sure whitespaces on the left or right of the user input
    # are not 'playbacked'. Also, we might not want to convert two or more
    # consecutive whitespaces (only one) into three periods.
    #
    # Split: returns a list of the words in the string, regarding consecutive
    #        whitespaces as a single separator.
    # Join: returns a string made of the concatenation of the strings in the
    #       list, being the separator the string caller of the method.
    text = " ".join(text.split())

    # Just replace " " with "..."
    output = text.replace(" ", "...")

    return output

# ============================================================================
# MAIN
# ============================================================================
def main():

    # Print header
    print_header()

    # INPUT
    text = input(PROMPT)

    # correctly playbacks the text, making sure only the wanted whitespaces
    # are converted into three periods.
    output = playback(text)

    # OUTPUT
    print(f"{PREOUTPUT}{output}")

main()
