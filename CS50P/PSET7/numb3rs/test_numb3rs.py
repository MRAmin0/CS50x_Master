from numb3rs import validate


def test_ip():
    # validity check
    assert validate("255.255.255.255") == True
    assert validate("192.168.1.1") == True
    assert validate("192.168.1.255") == True
    assert validate("0.0.0.0") == True
    assert validate("192.168.2") == False
    assert validate("192.168.1.256") == False
    assert validate("amin") == False
    assert validate("192.168.1.255.1") == False
    assert validate("400.400.400.400") == False
    assert validate("400.400.400.400.400") == False
    assert validate("amin.amin.amin.amin") == False
    assert validate("1.2.3.1000") == False
    assert validate("cow") == False
