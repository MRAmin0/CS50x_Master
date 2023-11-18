import string
import re


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    pattern = r"^[A-Za-z]{2}[A-Za-z1-9]{0,1}[A-Za-z0-9]{0,1}$"
    pattern_2 = (
        r"^[A-Za-z]{2}[A-Za-z]{0,1}[A-Za-z]{0,1}[A-Za-z1-9]{0,1}[A-Za-z1-9]{0,1}$"
    )

    if re.match(pattern, s) or re.match(pattern_2, s):
        return bool

    for char in string.punctuation:
        if char in s:
            return False


if __name__ == "__main__":
    main()
