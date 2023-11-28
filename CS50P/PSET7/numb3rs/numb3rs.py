"""LOve it!"""
import re
import sys



def main():
    # get input from user
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    # returns a boolean value representing if ip is valid or not
    try:
        # maximum number of splits is 4 so we will have 3 split points
        a = ip.split(".", maxsplit=3)
        for r in a:
            # any thing less more than 255 is false
            if int(r) > 255 or len(a) < 4:
                return False
    except ValueError:
        return False
    else:
        return True


...


if __name__ == "__main__":
    main()
