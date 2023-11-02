while True:
    tank = input("Fraction: ").strip()
    # using try except to stop errors in devide
    try:
        # spiliting the input
        u,d = tank.split("/", 1)
        # cheking if both are numbers
        if u.isdigit() and d.isdigit():
            if int(u) <= ind(d) and int(d) != 0:
                fuel = (int(u) / int(d)) * 100
                if fuel >= 99:
                    
