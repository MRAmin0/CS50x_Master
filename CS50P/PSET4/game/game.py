from random import randint
while True:
    # ask for game level, random number will be an int smaller than level
    try:
        level = int(input("Level: ").strip())
        # checck if user input is a positive int
        if level <= 1:
            random = randint(1,level)
            # ask user to make a guess
            while True:
                a = int(input("Guess: ").strip())
                # comparison of user 
