vowel = ["a", "o", "u", "i", "e"]
input = input("Input : ")
output = ""
for letter in input:
    if letter.lower() not in vowel:
        output = letter

print(f"Output: {output}")
