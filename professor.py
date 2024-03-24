from random import randint

levellist = [{1: [0, 9]}, {2: [10, 99]}, {3: [100, 999]}]


def main():
    slevel = get_level()
    pset = generate_integer(slevel)

    done = 0

    for question in pset:
        life = 0
        while True:
            try:
                answer = int(input(f"{question} = "))
                a, b = question.strip(" ").split("+")

                if life == 2:
                    print("EEE")
                    print(f"{question} = {(int(a)+ int(b))}")
                    break
                elif answer != (int(a) + int(b)):
                    life += 1
                    print("EEE")
                else:
                    done += 1
                    life = 0
                    break
            except ValueError:
                print("EEE")
                life += 1
                continue
    print(f"Score: {done}")


def get_level():
    while True:
        try:
            level = int(input())
            if level <= 3 and level > 0:
                return level
        except ValueError:
            continue


def generate_integer(level):
    pset = []

    lower = levellist[level - 1][level][0]
    higher = levellist[level - 1][level][1]

    for _ in range(0, 10):
        pset.append(f"{randint(lower, higher)} + {randint(lower, higher)}")

    return pset


if __name__ == "__main__":
    main()
