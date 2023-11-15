import inflect

p = inflect.engine()
names = []

while True:
    # getting user input
    try:
        a = str(input().strip())
        names.append(a)
        # wait for CTRL D to stop the code
    except (EOFError, KeyError):
        print(f"Adieu, adieu, to {p.join(names)}", end="\n")
        quit()
