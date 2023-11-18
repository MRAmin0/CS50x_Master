import string
import re


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    pattern = r"^[A-Za-z]{2}[A-Za-z1-9]?[A-Za-z0-9]?$"

    if re.match(pattern, s):
        return True

    for char in string.punctuation:
        if char in s:
            return False

    return False


if __name__ == "__main__":
    main()
