import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    # extract youtube link from embed
    try:
        # positive look behind
        url = re.search('(?<=embed\/).*?(?=")', s)
        return "https://youtu.be/" + url.group(0)

    except Exception:
        return None


if __name__ == "__main__":
    main()
