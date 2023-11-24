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
        scourgify(sys.argv[1], sys.argv[2])


def scourgify(input_file, output_file):
    # open input file amd write the final version to output
    with open(input_file, "r") as csv_file:
        cdata = csv.DictReader(csv_file, delimiter=",")
        # open input file amd write the final version to output
    with open(output_file, "w") as csv_file:
        cdata = csv.DictReader(csv_file, delimiter=",")

if __name__ == "__main__":
    main()
