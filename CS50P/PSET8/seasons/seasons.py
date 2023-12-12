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
    
if __name__ == "__main__":
    main()
