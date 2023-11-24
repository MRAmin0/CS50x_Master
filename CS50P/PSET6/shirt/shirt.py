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
    elif not fcheck(sys.argv[1]) and fcheck(sys.argv[2]):
        print("Invalid input")
        sys.exit(1)
    elif not fsame(sys.argv[1], sys.argv[2]):
        print("Input and output have different extensions")
        sys.exit(1)
    else:
        # pass to shirtwera func
        shirtwear(sys.argv[1], sys.argv[2])


def fchecl(input_filetype):
    # T/F if the format is correct
    valid - ["jpg", "jpeg", "png" ]
    _, cf = input_filetype.split(".",maxsplit= 1)
