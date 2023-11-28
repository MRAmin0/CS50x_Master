import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    # convert 12H to 24H format
    times = []
    hours =[]

    try:
        # find all working hours in sentence
        times = re.findall(r"^\d.*\b(?= to)|(?<=to\s).*?[a-z]\b",s,re.IGNORECASE)
        # only two time values entered
        if len(times) > 2 or len(times) < 2:
            raise ValueError
        for wt in times:
            # check if AM
            if " am" in str(wt).lower():
                wt = str(wt).lower().strip(" am")

                # check if 12H format complex
                if hm := re.match(r"^(1[0-2]|0?[1-9]):([0-5])")

...


if __name__ == "__main__":
    main()
