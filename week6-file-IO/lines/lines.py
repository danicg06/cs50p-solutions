import sys

def input_file():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if sys.argv[1].endswith(".py"):
        return sys.argv[1]
    else:
        sys.exit("Not a Python file")


def count_lines(file):
    try:
        counter = 0
        with open(file, 'r') as file:
            for line in file:
                if not line.isspace() and not line.lstrip().startswith("#"):
                    counter += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    return counter

def main():
    file = input_file()

    counter = count_lines(file)

    print(f"{counter}")

if __name__ == "__main__":
    main()


