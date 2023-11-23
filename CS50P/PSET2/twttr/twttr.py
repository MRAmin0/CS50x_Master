vowel = ["a", "o", "u", "i", "e"]
input = input("Input : ").strip()
output = ""
for letter in input:
    if letter.lower() not in vowel:
        output += letter

print(f"Output: {output}")
def main():
    ...


def shorten(word):
    ...


if __name__ == "__main__":
    main()