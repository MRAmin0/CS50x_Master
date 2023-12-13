import pytest
from jar import Jar

def test_init():
    # class initializes intance objecct (manually and automatically)
    jartest = Jar(9000,8999)
    ass

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


