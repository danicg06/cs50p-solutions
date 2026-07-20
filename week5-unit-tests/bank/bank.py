"""
bank.py - Greeting to payment.

This module implements a solution for the "Home Federal Saving Banks" problem
of the CS50, which prompts the user for a greeting.
If the greeting starts with "hello" (case-insensitively), there is no payment;
if the greeting starts with "h" (not the previous case), the bank pays the user
$20; otherwise, the payment is $100.

Author:
    Daniel Casasola Guerrero <danicg06>

Example:
    >>> python bank.py

    ----------
       BANK
    ----------

    Greeting: heLLo!
    $0
"""

# ============================================================================
# CONSTANTS
# ============================================================================

HEADER = """
----------
   BANK
----------
"""

PROMPT = ("Greeting: ")


# ============================================================================
# FUNCTIONS
# ============================================================================
def print_header():
    """
Prints the corresponding header, declared right above as a constant string.
"""
    print(HEADER)


def value(greeting):
    """
Calculates the corresponding amount of money the bank has to pay the customer
for the greeting.
"hello"          -> $0
"h*" (not hello) -> $20
other greeting   -> $100

Parameters:
greeting - string of the corresponding greeting.

Return value:
output - amount of money for the greeting (dollars).
"""
    # removes the leading and trailing whitespaces from the answer.
    # By the way, the problem remarked to ignore the leading whitespaces.
    greeting = greeting.strip()

    # converts the answer into lowercase just to check the greeting easier.
    greeting = greeting.lower()

    # calculates the corresponding payment
    if greeting.startswith("h"):
        if greeting.startswith("hello"):
            output = 0
        else:
            output = 20
    else:
        output = 100


    return output

# ============================================================================
# MAIN
# ============================================================================
def main():

    # Print header
    print_header()

    # INPUT
    greeting = input(PROMPT)

    # calculates the corresponding payment
    output = int(greeting_amount(greeting))

    # OUTPUT
    print(f"${output}")

if __name__ == "__main__":
    main()

