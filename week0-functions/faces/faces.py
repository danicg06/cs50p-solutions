"""
faces.py - Text to emoji face.

This module implements a solution for the "faces" problem of the CS50,
which converts the text ":)" (respectively, ":(") to 🙂 (respectively, 🙁)).
Any other text should not be changed.

Author:
    Daniel Casasola Guerrero <danicg06>

Example:
    >>> python faces.py

    --------------------
     TEXT TO EMOJI FACE
    --------------------

    Text: I feel :) horrible today :(
      ->  I feel 🙂 horrible today 🙁
"""

# ============================================================================
# CONSTANTS
# ============================================================================

HEADER = """
--------------------
 TEXT TO EMOJI FACE
--------------------
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

def convert(text):
    """
Converts any text by replacing ":)" or ":(" with 🙂 or 🙁, respectively.
Also, it removes the leading and trailling whitespaces of the string.

Parameters:
text - string to convert.

Return value:
output - string received as a parameter but with the expected changes.
"""
    # Remove leading and trailling whitespaces of the string 'text'
    output = text.strip()

    # Replaces ":("
    output = output.replace(":(", "🙁")

    # Replaces ":)"
    output = output.replace(":)", "🙂")

    return output

# ============================================================================
# MAIN
# ============================================================================
def main():

    # Print header
    print_header()

    # INPUT
    text = input(PROMPT)

    # correctly converts the string by replacing ":)" with 🙂 or ":(" with 🙁
    output = convert(text)

    # OUTPUT
    print(f"{PREOUTPUT}{output}")

main()
