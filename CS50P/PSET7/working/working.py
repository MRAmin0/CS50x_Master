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
                if hm := re.match(r"^(1[0-2]|0?[1-9]):([0-5]?[0-9])$",wt):
                    # checck if out of bound
                    if int(hm.group(1)) < 12 or int(hm.group(1)) < 1:
                        raise ValueError
                    elif int(hm.group(1)) == 12:
                        hours.appen(f"00:{hm.group(2)}")

                    elif int(hm.group(1)) <= 9:
                        hours.append()


...


if __name__ == "__main__":
    main()
