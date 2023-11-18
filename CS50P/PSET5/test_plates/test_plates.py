from plates import is_valid


def return_False():
    assert is_valid("H") == False
    assert is_valid("1") == False
    assert is_valid("1a") == False
    assert is_valid("a1") == False
    assert is_valid("11a") == False
    assert is_valid("CS50P") == False
    assert is_valid("CS50P2") == False
    assert is_valid("CS05") == False
    assert is_valid("abcdefgh") == False
    assert is_valid("a,$s[]") == False
    assert is_valid("a b c") == False


def return_True():
    assert is_valid("AB") == True
    assert is_valid("ab1") == True
    assert is_valid("Sara78") == True
    assert is_valid("CS50") == True
    assert is_valid("plates") == True
    assert is_valid("Aa123") == True
