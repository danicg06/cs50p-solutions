"""
grocery.py - Grocery list.

This module implements a solution for the "Grocery List" problem of CS50,
which prompts the user for items, one per line, until the user inputs
"control-d". Finally, outputs a grocery list in all uppercase, sorted
alphabetically by item and prefixing them by the number of times that they
were inputted.

Author:
    Daniel Casasola Guerrero <danicg06>

Example:
    >>> python grocery.py

    - To buy:
    banana
    apple
    strawberries
    apple

    --------------
     GROCERY LIST
    --------------

    2 APPLE
    1 BANANA
    1 STRAWBERRIES

"""

# ============================================================================
# CONSTANTS
# ============================================================================

HEADER2 = """
--------------
 GROCERY LIST
--------------
"""

HEADER1 = "- To buy:"

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

def get_list():
    """
    Prompts the user for an item of the list until a "control-d" is entered.
    Then, outputs every item added to the list prefixed by the number of times
    that it was inputted.

    Return value:
        output - string with the corresponding grocery list.
    """
    # dictionary that stores the number of times that a key has been inputted.
    grocery_list = dict()

    # prompts the user until "control-d" is entered.
    while True:
        try:
            item = input()

            # removes the leading and trailing whitespaces from the input.
            item = item.strip()

            # the user input is treated case-insensitively.
            # It is assumed that the dictionary is uppercase.
            item = item.upper()


            # if the item ordered is already in the dictionary.
            if item in grocery_list:
                grocery_list[item] += 1
            else: # if the item is not in the dictionary.
                grocery_list[item] = 1
        except EOFError:
            print("\n")
            break

    # alphabetically orders the dictionary list.
    grocery_list = dict(sorted(grocery_list.items()))

    output = ""

    if len(grocery_list) > 0:
        for item in grocery_list:
            output += f"{list[item]} {item}\n"

    return output


# ============================================================================
# MAIN
# ============================================================================
def main():

    # Print header
    print_header(HEADER1)

    # INPUT until the user enters "control-d"
    # returns the grocery list.
    output = get_list()

    # Print header
    print_header(HEADER2)

    # OUTPUT
    print(f"{output}")

if __name__ == "__main__":
    main()

