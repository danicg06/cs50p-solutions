"""
deep.py - Deep Thought.

This module implements a solution for the "Deep Thought" problem of the CS50,
which prompts the user for the answer to the Great Question of Life, the
Universe and Everything.
If the user inputs '42', 'forty two' or 'forty-two', it outputs 'Yes'.
Otherwise, the output is 'No'

Author:
    Daniel Casasola Guerrero <danicg06>

Example:
    >>> python deep.py

    --------------------
     THE GREAT QUESTION
    --------------------

    What is the answer to the Great Question of Life, the Universe and
    Everything? 42
    Yes
"""

# ============================================================================
# CONSTANTS
# ============================================================================

HEADER = """
--------------------
 THE GREAT QUESTION
--------------------
"""

PROMPT = ("What is the answer to the Great Question of Life, "
          "the Universe and Everything? ")


# ============================================================================
# FUNCTIONS
# ============================================================================
def print_header():
    """
Prints the corresponding header, declared right above as a constant string.
"""
    print(HEADER)


def answer_is_correct(answer):
    """
Checks if the given answer to the Great Question of Life is correct.
The answer must be "42", "forty two" or "forty-two" (case-insensitively) in
order to be the correct answer.

Parameters:
answer - string of the given answer by the user

Return value:
output - true if the answer is correct; otherwise, false.
"""
    # removes the leading and trailling whitespaces from the answer.
    answer = answer.strip()

    # converts the answer into lowercase just to check the answer easier.
    # Notice that only cased characters can be modified by lower(), so "42"
    # remains the same.
    answer = answer.lower()

    # output is true if the answer is correct, false otherwise.
    output = (answer == "42" or answer == "forty two" or answer == "forty-two")

    return output

# ============================================================================
# MAIN
# ============================================================================
def main():

    # Print header
    print_header()

    # INPUT
    answer = input(PROMPT)

    # if the user is right, the return value is "Yes".
    # otherwise, the return value is "No".
    if answer_is_correct(answer):
        output = "Yes"
    else:
        output = "No"

    # OUTPUT
    print(f"{output}")

if __name__ == "__main__":
    main()

