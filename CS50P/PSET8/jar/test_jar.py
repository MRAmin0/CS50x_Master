import pytest
from jar import Jar

def test_init():
    # class initializes intance objecct (manually and automatically) check
    jartest = Jar(9000,8999)
    assert jartest.capacity == 9000
    assert jartest.size == 8999

    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    ...


def test_withdraw():
    ...


