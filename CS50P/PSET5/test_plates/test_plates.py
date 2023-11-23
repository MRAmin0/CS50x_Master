from plates import is_valid


def test_s():
    # must start with at least two letters
    assert is_valid("123") == False
    assert is_valid("225") == False
    assert is_valid("AA2") == True


def test_s():
    # contain a maximum of 6 chars and a minimum of 2 chars
    assert is_valid("C") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("AA2") == True
