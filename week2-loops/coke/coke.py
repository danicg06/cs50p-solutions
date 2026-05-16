"""
coke.py - Coke machine.

This module implements a solution for the "Coke Machine" problem of CS50,
which sets an initial price for the coke, 50 cents. Then, it prompts the user to
insert a coin of 25, 10 or 5 cents, one at a time, informing the user of the
amount due or the change owed.
It is assumed that the user's input is an integer every time.

Author:
    Daniel Casasola Guerrero <danicg06>

Example:
    >>> python coke.py

    --------------
     COKE MACHINE
    --------------

    Amount Due: 50
    Insert Coin: 25
    Amount Due: 25
    Insert Coin: 10
    Amount Due: 5
    Insert Coin: 25
    Change Owed: 20

"""

# ============================================================================
# CONSTANTS
# ============================================================================

HEADER = """
--------------
 COKE MACHINE
--------------
"""

PROMPT = "Insert Coin: "

AMOUNT_PREOUTPUT = "Amount Due: "

CHANGE_PREOUTPUT = "Change Owed: "

INITIAL_PRICE = 50


# ============================================================================
# FUNCTIONS
# ============================================================================
def print_header():
    """
Prints the corresponding header, declared right above as a constant string.
"""
    print(HEADER)


def accepted_coin(coin):
    """
Returns true if the coin is 25, 10 or 5 cents. Otherwise, returns false.

Parameters:
coin - integer of coin introduced.

Return value:
output - true if the coin is accepted; otherwise, false.
"""
    match coin:
        case 25 | 10 | 5:
            output = True
        case _:
            output = False

    return output


def coke_machine(price):
    """
Sells the user a coke for the price of <price>. It prompts the user to insert a
coin until the coke is paid. In each insertion, the coke machine tells the user
the amount due or the change owed.
It must be assumed that the user's coin and the price is an integer.

Parameters:
price - integer of the coke's price.

Void function - no return value.
"""

    # variable for the total cents introduced by the user
    amount = 0

    # while the coke is not paid.
    while True:
        # prompts the user to insert a coin that has to be 25, 10 or 5 cents.
        # if not, it prompts the user again.
        # read-ahead.
        while True:
            coin = int(input(PROMPT))
            if accepted_coin(coin):
                break # leaves the loop

        # adds the introduced coin to the total amount paid.
        amount += coin

        # if the coke is paid.
        if amount >= price:
            break

        # if there is still some amount due.
        print(f"{AMOUNT_PREOUTPUT}{price-amount}")

    # if the amount paid is bigger than the coke price.
    print(f"{CHANGE_PREOUTPUT}{amount-price}")

# ============================================================================
# MAIN
# ============================================================================
def main():

    # Print header
    print_header()

    # In this case, the function <coke_machine> does the entire job: it manages
    # the input and the outputs.
    # Normally, it is not recommended to have an "input" and "output" function.
    # However, in this special case, it might be implemented this way.
    coke_machine(INITIAL_PRICE)

if __name__ == "__main__":
    main()

