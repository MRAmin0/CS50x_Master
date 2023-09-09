import string
from cs50 import get_string

# get user text
text = get_string("Text: ")

letters = 0
words = 1
sentences = 0

# count number of letters words and sentences
for i in text:
    if i.isalpha():
        letters += 1
    elif i == " ":
        words += 1
    elif i == "." or i == "!" or i == "?":
        sentences += 1

L = 100 * (letters / words)
S = 100 * (sentences / words)
# Coleman-Liau Index
index = round(0.0588 * L - 0.296 * S - 15.8)
if index >= 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {index}")
