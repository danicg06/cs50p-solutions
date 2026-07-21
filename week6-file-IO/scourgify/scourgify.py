import sys
import csv

def input_file():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if sys.argv[1].endswith(".csv"):
        return sys.argv[1]
    else:
        sys.exit("Not a CSV file")

def csv_converter(before_file, after_file):
    try:
        with open(before_file, 'r') as file:
            reader = csv.DictReader(file)

            with open(after_file, "w") as output:
                fields = ["first", "last", "house"]
                writer = csv.DictWriter(output, fieldnames = fields)
                writer.writeheader()

                for row in reader:
                    last, first = row["name"].split(",")
                    writer.writerow({"first": first.strip(), "last": last.strip(), "house": row["house"]})

    except FileNotFoundError:
        sys.exit("File does not exist")


def main():

    before_file = input_file()

    csv_converter(before_file, sys.argv[2])


if __name__ == "__main__":
    main()

