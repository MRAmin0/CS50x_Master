from CS50P.PSET5.test_plates.plates import is_valid

#All vanity plates must start with at least two letters.
def test_begintwoletters():
    assert is_valid("CS") == True
    assert is_valid("50") ==False
    assert is_valid("C5") ==False
    assert is_valid("5")  == False

# vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
def test_length():

    assert is_valid("HICSSB") -
    assert is_valid("CS")
True
16 17 assert is_valid("HELLOCSSO")
18
False
▷ style50
Salar
19 Numbers cannot be used in the middle of a plate; they must come at the end.
28 For example, AAA222 would be an acceptable vanity plate; AAA22A would not be acceptable.
21# The first number used cannot be a 'e',
22 def test mm():
tes.py
23 assert is_valid("MA222") True
plates.py
I
24 assert is_valid("AAA22A") False False
25 assert is_valid("AAA822")
26
27
28 No periods, spaces, or punctuation marks are allowed.
29 def test punct():
30 assert is_valid("CS50!")
31
False
