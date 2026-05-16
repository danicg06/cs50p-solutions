"""
einstein.py - Mass to Joules.

This module implements a solution for the "Einstein" problem of the CS50,
which calculates the energy as Einstein did, E = mc².
The user is prompted for an integer that represents the mass (kg).

Author:
    Daniel Casasola Guerrero <danicg06>

Example:
    >>> python einstein.py

    --------------------
     ENERGY CALCULATOR
    --------------------

    m(Kg): 4
    E(J): 360000000000000000
"""

# ============================================================================
# CONSTANTS
# ============================================================================

HEADER = """
-------------------
 ENERGY CALCULATOR
-------------------
"""

PROMPT    = "m(Kg): "

PREOUTPUT = "E(J):  "

C = 300000000 # speed of light, measured in m/s.


# ============================================================================
# FUNCTIONS
# ============================================================================
def print_header():
    """
Prints the corresponding header, declared right above as a constant string.
"""
    print(HEADER)

def energy(mass):
    """
Calculates the corresponding energy by the Einstein formula: E = mc².

Parameters:
mass - integer that represents the mass.

Return value:
energy - integer that represents the resultant energy.
"""
    # We ensure that mass is an integer, as it is assumed in the problem.
    m = int(mass)

    # E = mc²
    # pow(base, exp): returns 'base' to the power of 'exp'.
    energy = m*pow(C,2)

    return energy

# ============================================================================
# MAIN
# ============================================================================
def main():

    # Print header
    print_header()

    # INPUT (integer)
    mass = int(input(PROMPT))

    # calculates the energy corresponding to the given mass
    output = energy(mass)

    # OUTPUT
    print(f"{PREOUTPUT}{output}")

main()
