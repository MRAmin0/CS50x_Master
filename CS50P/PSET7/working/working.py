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
                        hours.append(f"00:{hm.group(2)}")

                    elif int(hm.group(1)) <= 9:
                        hours.append(f"0{hm.group(1)}:{hm.group(2)}")



                    else:
                        hours.append(f"0{hm.group(1)}:{hm.group(2)}")
                # check if 12H simple time
                elif hh := re.match(r"^(1[0-2]|0?[1-9])",wt):
                    if int(wt) > 12 or int(wt) < 1:
                        raise ValueError
                    elif int(hh.group(1)) == 12:
                        hours.append(f"00:00")

                    elif int(hh.group(1)) <= 9:
                        hours.append(f"0{hh.group(1)}:00")

                    else:
                        hours.append(f"{hh.group(1)}:00")
                else:
                    raise ValueError

            #check if PM
            if " pm" in str(wt).lower():
                wt = str(wt).lower().strip(" am")
                # check if 12H format complex
                if hm := re.match(r"^(1[0-2]|0?[1-9]):([0-5]?[0-9])$",wt):
                    # checck if out of bound
                    if int(hm.group(1)) > 12 or int(hm.group(1)) < 1:
                        raise ValueError
                    elif int(hm.group(1)) == 12:
                        hours.append(f"12:{hm.group(2)}")
                    else:
                        hours.append(f"{int(hm.group(1)) + 12}:{hm.group(2)}")


                 # check if 12 hour simple time
                elif hh := re.match(r"^(1[0-2]|0?[1-9])",wt):

                    # check if out of bound
                    if int(wt) > 12 or int(wt) < 1:
                        raise ValueError

                    elif int(hh.group(1)) == 12:
                        hours.append(f"12:00")
                    else:
                        hours.append(f"{int(hh.group(1)) + 12}:00")
                else:
                    raise ValueError
 




if __name__ == "__main__":
    main()
