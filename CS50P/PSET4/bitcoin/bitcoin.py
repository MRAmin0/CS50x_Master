import sys
import request

apilink = "https://api.coindesk.com/v1/bpi/currentprice.json"


def main():
    # user ask for bitcoin pride using argv
    print(f"${coindesk(testinput()):,.4f}")


def testinput():
    # check if user input is currect
    try:
        if len(sys.argv) < 2:
            print("Missing command-line argument")
            sys.exit(1)
        elif not float(sys.argv[1]):
            print("Command-line argument is not a number")
            sys.exit(1)
        else:
            return float(sys.argv[1])

        # error when input is not a number
    except (TypeError, ValueError):
        print("Command-line argument is not a number")
        sys.exit(1)


def coindesk(uinput):
    # send request to API and get the data
    try:
        response = requests.get(apilink)
        a = response.json()
        b = a["bpi"]["USD"]["rate_float"]
        c = uinput * b

    # Can't connect to API
    except requests.RequestException:
        print("CONNECTION ERROR")
        sys.exit()
    return c

if name = "__name__":
    main()

