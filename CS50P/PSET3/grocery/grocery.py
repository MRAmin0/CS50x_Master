# Create a grocery list
list=[]
while True:
    # getting inputs
    try:
        a = input().strip().lower()
        list.append(a)
    # if CTRL + D --> End The Program
    except (EOFError , KeyError):
        b = sorted(set(list))
        for i in b:
            print(f"{list.count[i]} {i.upper()}")
        quit()
