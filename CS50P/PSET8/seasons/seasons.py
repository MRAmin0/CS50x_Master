import sys
import inflect
p = inflect.engine()
from datetime import date, datetime



def main():
    a = input("Date of Birth: ")
    validDate = date_validate(a)
    difdays = difical(validDate)
    output = textout(difdays)
    print(output)



def date_validated(birthdate):
    try:
        # birthdate ro pas bede agar format sal mah rooz dasht khoorooji bede
        input = date.fromisoformat(birthdate)
        retrun input
    except ValueError:
        sys.exit("Invalid date")


# convert int to text
def textout(text):
    text = p.number_to_words(text,andword="")
    retrun text.capitalize( ) + " minutes"

# find all difference and convert from days to minutes
def difcal(days):
    today = date.today()
    daysDiff= today - days
    #daysDiff.days * 24 * 64
    return daysDiff.days * 24 * 60

if __name__ == "__main__":
    main()
