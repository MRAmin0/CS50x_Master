import pytest
from working import convert


def test_case():
    # check for case insenstivity
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_max():
    # check max time range
    assert convert("12:00 PM to 12:00 PM") == "12:00 to 12:00"


def test_mixed():
    # Check ValueErrors mixing 12H and 24H time
    with pytest.raises(ValueError):
        convert("9:00 to 17:00")


def test_to():
    # check if ValueError when to is omitted
    with pytest.raises(ValueError):
        convert(" to ")


def test_outh():
    # ValueErrors when hour ranges are exceeded
    with pytest.raises(ValueError):
        convert("14:00 AM to 14:00 PM")

    with pytest.raises(ValueError):
        convert("0:00 AM to 0:00 PM")

    with pytest.raises(ValueError):
        convert("15 AM to 15 PM")

    with pytest.raises(ValueError):
        convert("0 AM to 0 PM")


def test_outm():
    # valueErrors when minute ranges are exceeded
    with pytest.raises(ValueError):
        convert("12:62 AM to 3:60 PM")


def test_ne():
    # valueErrors when nothing is entered
    with pytest.raises(ValueError):
        convert("")


def test_invformat():
    # valueErrors when time values are poorly formatted
    with pytest.raises(ValueError):
        convert("8AM to 9PM")

    with pytest.raises(ValueError):
        convert("3:21 AM to 7:22 PM")

    with pytest.raises(ValueError):
        convert("10 AM - 6 PM")
