import pytest
from seasons import textout


def test_seasons():
    assert (
        textout(10477)
        == "Fifteen million, eighty-six thousand, eight hundred eighty minutes"
    )
    assert textout(365) == "Five hundred twenty-five thousand, six hundred minutes"
