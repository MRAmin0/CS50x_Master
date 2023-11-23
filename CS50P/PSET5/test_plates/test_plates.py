from plates import is_valid


def test_s():
    # must start with at least two letters
    assert is_valid("123") == False
    assert is_valid("11AA22") == False
    assert is_valid("225") == False
    assert is_valid("AA2") == True


def test_m():
    # contain a maximum of 6 chars and a minimum of 2 chars
    assert is_valid("C") == False
    # return False if the chars are 7
    assert is_valid("ABCDEFG") == False
    assert is_valid("ABCDEF") == True


def test_n():
    # numbers cannot be used in the middle
    assert is_valid("123456") == False
    assert is_valid("123ABC") == False
    assert is_valid("XXX012") == False
    assert is_valid("AB12C3") == False
    assert is_valid("AC12BB") == False
    assert is_valid("ABC678") == True


def test_symbols():
    # No periods , spaces , or punctuation marks are allowed
    assert is_valid("ABC?!-") == False
    assert is_valid(". 12[]") == False
    assert is_valid("/B^B3*") == False
    assert is_valid("A,B—!C") == False
