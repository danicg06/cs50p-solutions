import sys
import csv
from tabulate import tabulate

def input_file():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if sys.argv[1].endswith(".csv"):
        return sys.argv[1]
    else:
        sys.exit("Not a CSV file")

def pizza_table(file):
    info = []
    try:
        with open(file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                info.append({"Pizza": row[0], "Small": row[1], "Large": row[2]})

    except FileNotFoundError:
        sys.exit("File does not exist")

    return tabulate(info, headers="firstrow", tablefmt="grid")

def main():

    file = input_file()

    table = pizza_table(file)

    print(f"{table}")

if __name__ == "__main__":
    main()
