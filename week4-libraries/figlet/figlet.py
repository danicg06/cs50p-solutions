"""
figlet.py - Frank, Ian and Glen’s Letters.

This module implements a solution for the "Figlet" problem of CS50, which prompts
the user for a text to convert into another font depending on the number of
arguments expected:
- zero arguments: output text in a random font.
- two arguments: the arguments should be the following:
    python figlet.py [(-f|--font) <font>]
If the first argument or the second argument is not any of the required, the
program exits with an error message.

Author:
    Daniel Casasola Guerrero <danicg06>

Example:
    >>> python figlet.py

    ----------------
     FONT CONVERTER
    ----------------

    Input: HOUSE
    Output:
    ##
    ##      ####  ##  ##  #####  ####
    #####  ##  ## ##  ## ##     ##  ##
    ##  ## ##  ## ##  ##  ####  ######
    ##  ## ##  ## ##  ##     ## ##
    ##  ##  ####   ##### #####   ####


"""

# ============================================================================
# CONSTANTS
# ============================================================================

HEADER = """
----------------
 FONT CONVERTER
----------------
"""

PROMPT = "Input: "

PREOUTPUT = "Output: "

ERROR = "Use: python figlet.py [(-f|--font) <font>]"

# ============================================================================
# LIBRARIES
# ============================================================================
from pyfiglet import Figlet  # Figlet
import sys                   # sys
from random import choice    # choice
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


def change_font(PROMPT):
    """
    Prompts the user for a text to change its font.

    Arguments:
        PROMPT - global constant string of the corresponding prompt.

    Return value:
        output - string of the corresponding converted text.
    """

    selected_font = False

    if len(sys.argv) > 1:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":

            figlet = Figlet()
            selected_font = True
            if sys.argv[2] not in figlet.getFonts():
                sys.exit(ERROR)
        else:
            sys.exit(ERROR)

    # if first argument is not -f or --font, or it is but the second argument
    # is not a valid font.
    text = input(PROMPT)
    figlet = Figlet()
    if selected_font:
        figlet.setFont(font = sys.argv[2])
    else:
        figlet.setFont(font = choice(figlet.getFonts()))

    return figlet.renderText(text)


# ============================================================================
# MAIN
# ============================================================================
def main():

    # Print header
    print_header(HEADER)

    # INPUT the user for a text
    # Returns the text with the font changed
    output = change_font(PROMPT)

    print(f"{PREOUTPUT}{output}")

if __name__ == "__main__":
    main()

