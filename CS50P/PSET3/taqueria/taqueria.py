menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

b = 0
while True:
    # make user imput like menu and print total
    try:
        a = input("Item: ").strip().title()
        if a in menu:
            b += menu[a]
            print(f"${b:.2f}")
            # if CTRL + D is pressed then exit the program
    except (EOFError, KeyError):
        print("", end="\n")
        quit()
