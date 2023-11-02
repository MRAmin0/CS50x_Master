a = input("camelCase: ").strip()
snake = ""
for letter in a:
    if letter.isupper():
        snake += "_"
        snake += letter.lower
    else:
        snake += letter

print(f"snake_case {snake}")
