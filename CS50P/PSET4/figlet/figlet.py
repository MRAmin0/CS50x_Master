import sys
from random import choice
from pyfiglet import Figlet

figlet = Figlet()
fonlist = figlet.getFonts()
# if there are no parameters in argv to be used as font choice
if len(sys.argv) == 1:
    a = input("Input: ").strip()
    figlet.setFont(font = choice(fontlist))
    print(figlet.renderText(a))
# if the arvg was complete and font could be recognized
elif len(sys.argv) == 3:
    if str(sys.argv[1]) in ["-f" , "--font"] and str(sys.argv[2]) in fontlist
