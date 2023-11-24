import os
import sys
import csv
from PIL import Image, ImageOps


def main():
    # check command-line arguments
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print(f"Could not read{sys.argv[1]}")
        sys.exit(1)
    else:
        # true mode
        scourgify((sys.argv[1]), sys.argv[2])


def tablemaker(user_input):
    # import CSV and make a table
    with open(user_input, "r") as csv_file:
        table = csv.DictReader(csv_file, delimiter=",")
        # pass table as dict and use keys as headers to make a table
        print(tabulate(table, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
