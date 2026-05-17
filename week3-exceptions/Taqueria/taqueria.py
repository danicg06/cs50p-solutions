"""
taqueria.py - Taqueria order.

This module implements a solution for the "Felipe's Taqueria" problem of CS50,
which prompts the user for an order until the user enters "control-d". If the
item is not sold by Felipe, then the user is forced to order another item.
The price of each item will be added to the total.

The menu is the following:

    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00


Author:
    Daniel Casasola Guerrero <danicg06>

Example:
    >>> python taqueria.py

    -------------------
     FELIPE'S TAQUERIA
    -------------------

    Item: bowl
    Total: $8.50
    Item: taco
    Total: $11.50

"""

# ============================================================================
# CONSTANTS
# ============================================================================

HEADER = """
-------------------
 FELIPE'S TAQUERIA
-------------------
"""

PROMPT = "Item: "

PREOUTPUT = "Total: $"

MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

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

def get_order(PROMPT):
    """
    Prompts the user for an order until a "control-d" is entered. In each order,
    the price is added to the total cost.

        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00


    Arguments:
        PROMPT - global constant string of the corresponding prompt.

    Void function - no return value.
    """
    # total cost is initially set to 0.
    total = 0

    # prompts the user until "control-d" is entered.
    while True:
        try:
            order = input(PROMPT)

            # removes the leading and trailing whitespaces from the input.
            order = order.strip()

            # the user input is treated case-insensitively.
            # It is assumed that the menu is titlecased.
            order = order.title()


            # if the item ordered is in the menu.
            if order in MENU:
                total += MENU[order]
                print(f"{PREOUTPUT}{total:.2f}")
        except EOFError:
            print("\n")
            break



# ============================================================================
# MAIN
# ============================================================================
def main():

    # Print header
    print_header(HEADER)

    # INPUT until the user enters "control-d"
    # calculates the total cost in each order.
    get_order(PROMPT)

if __name__ == "__main__":
    main()

