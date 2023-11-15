from random import randint

while True:
    # ask for game level, random number will be an int smaller than level
    try:
        level = int(input("Level: ").strip())
        # checck if user input is a positive int
        if level >= 1:
            random = randint(1, level)
            # ask user to make a guess
            while True:
                # comparison of user input and random generated number
                try:
                    a = int(input("Guess: ").strip())
                    if a > random:
                        print("Too large!")
                    elif a < random:
                        print("Too small!")
                    else:
                        print("Just right!")
                        break
                    # ask again for an input (guess) if it wasn't valid
                except (TypeError, ValueError):
                    continue
             break
    # ask again for an input (level) if it wasn't valid
    except (TypeError, ValueError):
        continue
