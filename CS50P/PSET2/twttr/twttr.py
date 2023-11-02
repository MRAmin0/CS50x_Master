vowel = ["a", "o", "u", "i", "e"]
input = input("Input : ").strip()
output = ""
for letter in input:
    if letter.lower() not in vowel:
        output = +letter.lower()
print(f"Output: {output}")
