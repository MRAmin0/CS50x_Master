# import string
# from cs50 import get_string

# text = get_string("Text: ")
# letters = 0
# for i in text:
#     if i.isalpha():
#         letters += 1

# # remove space in word
# word = len(text.split())
# sentences = 0
# for j in text:
#     if j == '.' or j == '?' or j == '!':
#         sentences += 1
# wordsentence = word / 100
# L = letters / wordsentence
# S = sentences / wordsentence
# index = round(0.588 * L - 0.296 * S - 15.8)
# if index < 1:
#     print("Before Grade 1")
# elif index >= 16:
#     print("Grade 16+")
# else:
#     print(f"Grade {index}")

import string
from cs50 import get_string

text = get_string("Text: ")
letters = 0

for char in text:
    if char.isalpha():
        letters += 1

# Remove space in word
word = len(text.split())
sentences = 0

for char in text:
    if char in ['.', '?', '!']:
        sentences += 1

# Avoid division by zero
if word == 0:
    print("No words found in the text.")
else:
    wordsentence = word / 100
    L = (letters / wordsentence) * 0.588
    S = (sentences / wordsentence) * 0.296
    index = round(0.0588 * L - 0.296 * S - 15.8)

    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")
