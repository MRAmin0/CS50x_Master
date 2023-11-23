from bank import value


def test_value_casesenstivity():
    # if input starts with "hello" return 0
    assert value("hello") == 0
    assert value("Hello") == 0



def test_value_firstletter():
    # if input starts with "h" but not hello return 20
    assert value("how u doing?") == 20
    assert value("hoo hoo hoo") == 20

def test_value_failure():
    # anything else return 100
    assert value("what does the fox say ?") == 100
    assert value("Amin") == 100
