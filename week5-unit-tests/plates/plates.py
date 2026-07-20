"""
plates.py - Validating vanity plates.

This module implements a solution for the "Vanity plates" problem of CS50, which
checks if the vanity plate introduced by the user is valid or not.
To be valid, a vanity plate must meet the following requirements:

·) “All vanity plates must start with at least two letters.”
·) “… vanity plates may contain a maximum of 6 characters (letters or numbers)
    and a minimum of 2 characters.”
·) “Numbers cannot be used in the middle of a plate; they must come at the end.
    For example, AAA222 would be an acceptable … vanity plate; AAA22A would not
    be acceptable. The first number used cannot be a ‘0’.”
·) “No periods, spaces, or punctuation marks are allowed.”

Also, it must be assumed that any letter of the user's input is uppercase.

Author:
    Daniel Casasola Guerrero <danicg06>

Example:
    >>> python plates.py

    --------------------------
     VALIDATING VANITY PLATES
    --------------------------

    Plate: 67HELLO
    False
"""

# ============================================================================
# CONSTANTS
# ============================================================================

HEADER = """
--------------------------
 VALIDATING VANITY PLATES
--------------------------
"""

PROMPT = "Plate: "


# ============================================================================
# FUNCTIONS
# ============================================================================
def print_header():
    """
Prints the corresponding header, declared right above as a constant string.
"""
    print(HEADER)

def third_req_plate(plate):

    # while loop for finding the first occurence of a number.
    index = 0
    while index < len(plate):
        if plate[index].isnumeric():
            break
        else:
            index+=1

    # if there is not any number in the plate, the condition is met.
    if index == len(plate):
        output = True
    # if a number has been found:
    # if the number is in the first character of the plate or it is a 0.
    elif (index == 0 or plate[index] == "0"):
        output = False
    else:
        # it is extracted the last characters of the plate from the calculated
        # index to the end.
        numbers_plate = plate[index-len(plate):]

        # if all characters of the substring are numbers,
        output = (numbers_plate.isnumeric())

    return output


def is_valid(plate):
    """
Checks if the parameter plate is a valid vanity plate with the following
requirements:

·) “All vanity plates must start with at least two letters.”
·) “… vanity plates may contain a maximum of 6 characters (letters or numbers)
    and a minimum of 2 characters.”
·) “Numbers cannot be used in the middle of a plate; they must come at the end.
    For example, AAA222 would be an acceptable … vanity plate; AAA22A would not
    be acceptable. The first number used cannot be a ‘0’.”
·) “No periods, spaces, or punctuation marks are allowed.”

It is assumed that plate is a string, same as that any letter of the input is
uppercase.

Parameters:
plate - string of the plate to be validated.

Return value:
output - true if the vanity plate is valid; otherwise, it is false.
"""
    # Notice that each requirement could have been checked by implementing
    # another function.
    # No other function except for the third condition is implemented just
    # because they can be checked in a single code line.

    # removes the leading and trailing whitespaces from the text.
    plate = plate.strip()

    # as it is assumed that the letters of the plate are uppercase, we ensure
    # that.
    plate = plate.upper()

    # by default, the vanity plate is not valid
    output = False

    ## checks the second requirement.
    pl_len = len(plate)
    req2 = (pl_len >= 2 and pl_len <= 6)

    # if the third requirement is fulfilled.
    if req2:
        ## checks the first requirement.
        req1 = (plate[0:2].isalpha())

        # if the first requirement is fulfilled.
        if req1:
            ## checks the last requirement.
            # to prove that there is no periods, spaces or punctuation marks,
            # the string has to be alphanumeric.
            req4 = (plate.isalnum())

            # if the last requirement is fulfilled.
            if req4:
                # checks the third requirement.
                req3 = third_req_plate(plate)

                # if the third requirement is fulfilled, then it is a valid
                # plate.
                if req3:
                    output = True

    # as we have initialized output as false, if any of the requirements is not
    # met, we already have the non-valid check, so there is no need to implement
    # an "else" clause.


    return output


# ============================================================================
# MAIN
# ============================================================================
def main():

    # Print header
    print_header()

    # INPUT
    plate = input(PROMPT)

    # converts the user's input into snake case.
    if is_valid_plate(plate):
        output = "Valid"
    else:
        output = "Invalid"

    # OUTPUT
    print(f"{output}")

if __name__ == "__main__":
    main()

