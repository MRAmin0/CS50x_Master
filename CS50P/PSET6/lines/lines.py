import sys

# we import os to get file Address
import os


def main():
    # p-file line counter
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
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
        # total line counter
        tlines = list(enumerate(lines.readlines(), start=1))

        # check if each line is code or not
        for nline, line in tlines:
            if (
                lines.strip().startswith("#")
                or lines.srtip().startswith("\n")
                or ines.isspace()
            ):
                rline += 1
    return int(tlines[-1][0]) - rline


if __name__ == "__main__":
    main()
