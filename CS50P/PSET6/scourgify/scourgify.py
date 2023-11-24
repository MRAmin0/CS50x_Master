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
    with open(input_file, "r") as csv_rfile:
        cdata = csv.DictReader(csv_rfile, delimiter=",")
        # open input file amd write the final version to output
    with open(output_file, "w") as csv_wfile:
        fname = ["first", "last", "house"]
        cw = csv.DictWriter(csv_wfile, fieldnames=fname)

        # write the header to output file
        cw.writeheader()

        # write source to output
        for i in cdata:
            last, first = i["name"].split(",")
            house = i["house"]

            cw.writerow({"first": first.strip(), "last": last, "house": house})


if __name__ == "__main__":
    main()
