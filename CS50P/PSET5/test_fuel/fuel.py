def main():
    while True:
        # left fuel input
        try:
            fraction = str(input("Fraction: ").strip())
            print(gauge(convert(fraction)))
            break
        except(ValueError,ZeroDivisionError,UnboundLocalError):
            continue


def convert(fraction):
    ...


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()

