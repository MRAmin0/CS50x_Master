from emoji import emojize

a = str(input("Input : ").strip())
print(f"Output: {emojize(a, language = 'alias')}")
