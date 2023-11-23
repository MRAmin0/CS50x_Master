import sys
# we import os to get file Address
import os


def main():
    #p-file line counter
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) >2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("File foes not exist")
        sys.exit(1)

    elif not sys.argv[1].endwith(".py"):
        print("Not a Python file")
        sys.exit(1)
    else:
        print(counter(sys.argv[1]))


def counter(python_file):
    # count deleting empty lines and comment lines
    rline = 0

    with open(python_file, "r") as lines:

        # 
