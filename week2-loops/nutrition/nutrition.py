"""
nutrition.py - Fruit calories.

This module implements a solution for the "Nutrition Facts" problem of CS50,
which prompts the user to input a fruit and returns its calories, based on
the "FDA's poster for fruits".

Author:
    Daniel Casasola Guerrero <danicg06>

Example:
    >>> python nutrition.py

    ---------------------------
     FRUIT CALORIES CALCULATOR
    ---------------------------

    Fruit: apple
    Calories: 130
"""

# ============================================================================
# CONSTANTS
# ============================================================================

HEADER = """
---------------------------
 FRUIT CALORIES CALCULATOR
---------------------------
"""

PROMPT = "Fruit: "

PREOUTPUT = "Calories: "

FRUITS = {
    "apple" : 130,
    "avocado" : 50,
    "banana" : 110,
    "cantaloupe" : 50,
    "grapefruit" : 60,
    "grapes" : 90,
    "honeydew melon" : 50,
    "kiwifruit" : 90,
    "lemon" : 15,
    "lime" : 20,
    "nectarine" : 60,
    "orange" : 80,
    "peach" : 60,
    "pear" : 100,
    "pineapple" : 50,
    "plums" : 70,
    "strawberries" : 50,
    "sweet cherries" : 100,
    "tangerine" : 50,
    "watermelon" : 80
}

# ============================================================================
# FUNCTIONS
# ============================================================================
def print_header():
    """
Prints the corresponding header, declared right above as a constant string.
"""
    print(HEADER)

def calories(fruit):
    """
Returns an integer as the number of calories the given fruit has in a portion.

Arguments:
fruit - string of the corresponding fruit.

Return value:
output - integer of the corresponding number of calories.
         If output is -1, then the given fruit is not in the dictionary.
"""

    # removes the leading and trailing whitespaces from the fruit's name.
    fruit = fruit.strip()

    # as the fruit names are in lowercase in the dict, it is ensured that
    # the input is in lowercase (because the problem is case-insensitive).
    fruit = fruit.lower()

    # if the given fruit is not in the dict, nothing is done.
    if fruit in FRUITS:
        output = int(FRUITS[fruit])
    else:
        output = -1

    return output

# ============================================================================
# MAIN
# ============================================================================
def main():

    # Print header
    print_header()

    # INPUT
    fruit = input(PROMPT)

    # calculates the fruit's calories per portion
    output = calories(fruit)

    # OUTPUT
    if output == -1:
        print("")
    else:
        print(f"{PREOUTPUT}{output}")

if __name__ == "__main__":
    main()

