import string
from cs50 import get_string
# get user text
text = get_string("Text: ")

letters = 0
words = 0
sentences = 0

# count number of letters words and sentences
for i in text:
    if i.isalpha():
        letters += 1

# remove space in word
words = len(text.split())
for j in text:
    if j == "." or j == "?" or j == "!":
        sentences += 1
wordsentence = words / 100
L = letters / wordsentence
S = sentences / wordsentence
index = round(0.588 * L - 0.296 * S - 15.8)
if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
