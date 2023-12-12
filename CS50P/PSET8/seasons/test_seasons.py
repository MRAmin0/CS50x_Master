import pytest
from seasons import textout


def test_seasons():
    assert textout("525600") == "Five Hundred twenty-five thousand six hundred minutes"
    assert textout("748523") == "Seven hundred forty-eight thousand five hundred twenty-three minutes"
