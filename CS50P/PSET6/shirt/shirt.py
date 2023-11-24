import os
import sys
from PIL import Image,ImageOps

def main():
    # check command-line arguments
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print(f"Invalid input - Path")
        sys.exit(1)
    elif not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)

    else:
        # true mode
        scourgify(sys.argv[1], sys.argv[2])
