"""
interpreter.py - Extensions to MIME type.

This module implements a solution for the "Math Interpreter" problem of the
CS50, which prompts the user for an arithmetic expression formatted as "x op y",
where x and y are integers, op is an operation (+, -, * or /) and there is a
single whitespace between x (or y) and op.
Notice that, if the operation is a division (op is /), then y cannot be 0. As
a consequence, it will be ensured that this situation is not possible.

Author:
    Daniel Casasola Guerrero <danicg06>

Example:
    >>> python interpreter.py

    ------------
     CALCULATOR
    ------------

    Expression: 6 / 2
    = 3.0
"""

# ============================================================================
# CONSTANTS
# ============================================================================

HEADER = """
------------
 CALCULATOR
------------
"""

PROMPT = ("Expression: ")

PREOUTPUT = "= "

NO_CORRECT_OPERATION = "The operation must be: +, -, * or /."

DIVIDE_BY_0 = "Cannot divide by 0."


# ============================================================================
# FUNCTIONS
# ============================================================================
def print_header():
    """
Prints the corresponding header, declared right above as a constant string.
"""
    print(HEADER)


def calculator(expression):
    """
Calculates the result of the given expression,
The expression must have the following format:
                x op y
being both x and y integers, op one of the following operations: +, -, * or /;
and only having a single whitespace between the integers and the operation
sign.

Parameters:
expression - string of the corresponding math expression (x op y).

Return value:
output - float value that refers to the solution of the expression.
"""
    # removes the leading and trailing whitespaces from the parameter file.
    expression = expression.strip()

    # splits the string expression into three strings, one for each integer
    # and operation.
    components = expression.split(" ")

    # we assume that the given expression is formatted as indicated.
    # if not, there could be an error for trying to access an invalid memory
    # address.
    integer1 = int(components[0])
    op       = components[1]
    integer2 = int(components[2])

    # checks if the operator is a division and the divisor is not 0.
    dividing_by_0 = (op == "/" and integer2 == 0)

    if not dividing_by_0:
        # we study the different cases of the operator.
        match op:
            case "+":
                output = float(integer1 + integer2)
            case "-":
                output = float(integer1 - integer2)
            case "*":
                output = float(integer1 * integer2)
            case "/":
                output = float(integer1 / integer2)
            case _:
                output = NO_CORRECT_OPERATION
    else:
        output = DIVIDE_BY_0

    return output

# ============================================================================
# MAIN
# ============================================================================
def main():

    # Print header
    print_header()

    # INPUT
    expression = input(PROMPT)

    # calculates the corresponding result of the math expression
    output = calculator(expression)

    # OUTPUT
    print(f"{PREOUTPUT}{output}")

if __name__ == "__main__":
    main()

