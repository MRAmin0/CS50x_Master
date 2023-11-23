def main():
    while True:
        # left fuel input
        try:
        tank = str(input("Fraction: ").strip())
        # using try except to stop errors in devide
        try:
            # spiliting the input
            u, d = tank.split("/", 1)
            # cheking if both are numbers
            if u.isdigit() and d.isdigit():
                if int(u) <= int(d) and int(d) != 0:
                    fuel = (int(u) / int(d)) * 100
                    if fuel >= 99:
                        print("F")
                        break
                    elif fuel < 99 and fuel > 1:
                        print(f"{fuel:.0f}%")
                        break
                    else:
                        print("E")
                        break
        except (ValueError, ZeroDivisionError):
            pass
        else:
            pass


def convert(fraction):
    ...


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()

