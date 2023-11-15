import sys
from random import choice
from pyfiglet import Figlet

figlet = Figlet()
fonlist = figlet.getFonts()
# if there are no parameters in argv to be used as font choice
if len(sys.argv) == 1:
    a = input("Input: ").strip()
    figlet.setFont(font=choice(fontlist))
    print(figlet.renderText(a))
# if the arvg was complete and font could be recognized
elif len(sys.argv) == 3:
    if str(sys.argv[1]) in ["-f", "--font"] and str(sys.argv[2]) in fonlist:
        a = input("Input: ").strip()
        figlet.setFont(font=str(sys.argv[2]))
        print(figlet.renderText(a))

    else:
        # happens when font is not found
        sys.exit("Invalid usage")
# happens when there is a problem with the whole input
else:
    sys.exit("Invalid usage")
