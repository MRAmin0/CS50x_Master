import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("0/1") == 0
    assert convert("1/1") == 100
    # assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/100") == 1

    # not int check
    with pytest.raises(ValueError):
        convert("x/y")

    # Zero devision check
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    # percentage return
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(3) == "3%"
    assert gauge(50) == "50%"
    # assert gauge(60) == "60%"
    # assert gauge(70) == "70%"
    assert gauge(74) == "74%"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
