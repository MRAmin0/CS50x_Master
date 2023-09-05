from cs50 import get_string
while True
    cardnum = get_string("Number: ")
    if cardnum.isnumeric():
        break
    else:
        continue

evens = 0
odds = 0

card = reversed([int(digit) for digit in cardnum])
# charkhidan be tedad monaseb
for i, digit in enumerate(card):
    if (i + 1) % 2 == 0:
        digitodd = digit *2
        if digitodd > 9:
            odds += int(digitodd /10) + digitodd % 10
        
