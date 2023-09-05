from cs50 import get_string
while True:
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
        else:
            odds += digitodd
    else:
        evens += digit

sum = evens + odds

start = int(cardnum[0:2])
cardlen = len(cardnum)
sld = sum % 10

if sld == 0:
    if start in [34,37] and cardlen == 15:
        print("AMERICAN EXPRESS")
    elif (start in range (51,56) and cardlen == 16):
        print("MASTERCARD")
    elif ((int(cardnum[0]) == 4) and cardlen in [13,16]):
        print("VISA")
else:
    print("INVALID")
