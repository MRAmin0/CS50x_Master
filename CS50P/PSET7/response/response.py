import validators

address = input("What's your email address? ").strip()

# check if the emial is valid using validators library
if validators.email(address):
    print("Valid")
else:
    print("Invalid")
# regex = "^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
