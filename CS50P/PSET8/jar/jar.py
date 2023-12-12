class Jar:
    def __init__(self, capacity=12, size =0):
        # initialize a cookie jar with the given capacoty
        self.capacity = capacity
        self.size = size

    def __str__(self):
        # return a str with 🍪, where is the number of cookies
        return "🍪" * self.size
    def deposit(self, n):
        # add n cookies to the cookie jar.
        if not n > (self.capacity )

    def withdraw(self, n):
        ...

from jar import Jar


def test_init():
    ...


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

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...
