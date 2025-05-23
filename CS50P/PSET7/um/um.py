import re
import sys


def main():
    # get input
    print(count(input("Text: ")))


def count(s):
    # return number of ums as an int
    return len(re.findall(r"^um\b|(?<=\s)um\b", s, re.IGNORECASE))


if __name__ == "__main__":
    main()
