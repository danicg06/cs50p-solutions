"""
extensions.py - Extensions to MIME type.

This module implements a solution for the "File Extensions" problem of CS50,
which prompts the user for the name of a file and then outputs that file's media
type. The allowed extensions are:
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip

Author:
    Daniel Casasola Guerrero <danicg06>

Example:
    >>> python extensions.py

    ---------------------
     MIME TYPE CONVERTER
    ---------------------

    File name: cs50.zip
    -> application/zip
"""

# ============================================================================
# CONSTANTS
# ============================================================================

HEADER = """
---------------------
 MIME TYPE CONVERTER
---------------------
"""

PROMPT = ("File name: ")

PREOUTPUT = "-> "


# ============================================================================
# FUNCTIONS
# ============================================================================
def print_header():
    """
Prints the corresponding header, declared right above as a constant string.
"""
    print(HEADER)


def MIME_type_calculator(file):
    """
Indicates the corresponding MIME type for the given file type.
The allowed file extensions are:
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip

Parameters:
file - string of the corresponding file.

Return value:
output - string of the corresponding MIME type.
"""
    # removes the leading and trailing whitespaces from the parameter file.
    file = file.strip()

    # converts the file name into lowercase because of case-insensitivity.
    file = file.lower()

    # calculates the corresponding MIME type.
    # In order to not use if/else + endswith() for each possible extension,
    # a possible idea can be: extract the extension from the file string and
    # use a 'match' to study the possible cases.
    #
    # rsplit(a, n): returns a list of string separated by "a", doing, at most, n
    # splits, couting form the end of the string.
    # list[k]: returns the element in the k position of the list.
    #          if k = -1, returns the last element in the list.
    if (file.find(".") != -1):
        extension = file.rsplit(".", 1)[-1]
    else:
        extension = ""

    match extension:
        case "gif":
            output = "image/gif"
        case "jpg" | "jpeg":
            output = "image/jpeg"
        case "png":
            output = "image/png"
        case "pdf":
            output = "application/pdf"
        case "txt":
            output = "text/plain"
        case "zip":
            output = "application/zip"
        case _:
            output = "application/octet-stream"

    return output

# ============================================================================
# MAIN
# ============================================================================
def main():

    # Print header
    print_header()

    # INPUT
    file = input(PROMPT)

    # calculates the corresponding MIME type
    output = MIME_type_calculator(file)

    # OUTPUT
    print(f"{output}")

if __name__ == "__main__":
    main()

