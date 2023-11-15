import sys
import request

apilink ="https://api.coindesk.com/v1/bpi/currentprice.json"

def main():
    # user ask for bitcoin pride using argv
    print(f"${coindesk(testinput()):,.4f}")


def testinput():
    # check if user input is currect
    try:
        if len(sys.argv) < 2:

