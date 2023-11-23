vowel = ["a", "e", "o", "u", "i"]


def main():
    input = str(input("Input : ").strip())
    print(f"Output: {shorten(input)}")


def shorten(word):
    output = ""
    # check all letters
    for letter in word:
        if letter.lower() not in vowel:
            output += letter

    return output


if __name__ == "__main__":
    main()
