# import pytest
# from jar import Jar


# def test_init():
#     # class initializes intance objecct (manually and automatically) check
#     jartest = Jar(9000, 8999)
#     assert jartest.capacity == 9000
#     assert jartest.size == 8999

#     jar = Jar()
#     assert jar.capacity == 12
#     assert jar.size == 0


# def test_capacity():
#     # class corectly initializes the jar capacity check
#     jar1test = Jar()
#     jar2test = Jar(10)

#     assert jar2test.capacity == 10
#     assert jar1test.capacity == 12

#     # manually can't be negative integer values.
#     with pytest.raises(ValueError):
#         test1 = Jar(-1)
#     with pytest.raises(ValueError):
#         test1 = Jar("dog")


# def test_size():
#     # new jar = 0
#     chocolate_cookie_jar = Jar()
#     crunchy_cookie_jar = Jar()

#     assert crunchy_cookie_jar.size == 0
#     assert chocolate_cookie_jar.size == 0

#     # check that jar size can not be manually instahtiated with new
#     with pytest.raises(ValueError):
#         double_fudge_brownies = Jar(12, -1)


# def test_deposit():
#     # check deposit and cookies
#     test1 = Jar(10)
#     test1.deposit(4)
#     assert test1.size == 4

#     check1 = Jar(12, 11)
#     with pytest.raises(ValueError):
#         check1.deposit(2)


# def test_capacity_property():
#     # capacity return total capacity if the instance
#     jartest1 = Jar(24)
#     assert jartest1.capacity == 24

#     def test_size_property():
#         # return the total size of the instance
#         jartest1 = Jar(24)
#         assert jartest1.capacity == 24


# def test_size_property():
#     # returns the total size of the instance
#     jartest1 = Jar(32)
#     jartest1.deposit(32)
#     jartest1.withdraw(12)
#     assert jartest1.size == 20


# def test_withdraw():
#     # withdraw remoevs correct
#     jartest1 = Jar(4)
#     jartest1.deposit(3)
#     jartest1.withdraw(2)
#     assert jartest1.size == 1

#     check1 = Jar(12, 11)
#     with pytest.raises(ValueError):
#         check1.withdraw(12)


# def test_str():
#     # __str__ returns right amount of cookie emojis.
#     jar = Jar()
#     assert str(jar) == ""

#     jar.deposit(1)
#     assert str(jar) == "🍪"

#     jar.deposit(3)
#     assert str(jar) == "🍪🍪🍪🍪"

#     jar.deposit(11)
#     assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

#     jar.withdraw(1)
#     assert str(jar) == "🍪🍪🍪"
import pytest
from jar import Jar


def test_init():
    jar = Jar()


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.deposit(20)


def test_withdraw():
    jar = Jar()
    jar.deposit(4)
    jar.withdraw(1)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(100)
