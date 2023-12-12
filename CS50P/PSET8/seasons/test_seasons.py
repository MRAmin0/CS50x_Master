import pytest
from seasons import date_validate, textout, difcalculate


def test_date_validate():
    with pytest.raises(ValueError):
        date_validate("June 1, 01")
    assert date_validate("1999-01-01") == "1999-01-01"
    assert date_validate("1998-11-15") == "1999-11-15"
    # assert date_validate("june 1, 01") == "Invalid date"
    # assert date_validate("2001-01-01") == "2001-01-01"


def test_difcalculate():
    assert difcalculate("2020-06-20") == "1774080"
    assert difcalculate("1998-11-15") == "13132800"
    assert difcalculate("2001-01-01") == "12012480"


def test_textout():
    assert (
        textout("1774080") == "One million, seven hundred seventy-four thousand eighty"
    )
