import pytest
from seasons import textout


def test_seasons():
    assert textout("525600") == "Five hundred twenty-five thousand, six hundred"
