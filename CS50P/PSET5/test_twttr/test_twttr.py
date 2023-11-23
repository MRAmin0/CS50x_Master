from twttr import shorten


def test_shorten():
    # test if it removes all vowels in a str
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("Amin") == "mn"
    assert shorten("Iran : The permanent land!") == "rn : Th Prmnnt lnd!"
    assert shorten("1aeu2b333cii4f5ea") == "12b333c4f5"
    assert shorten("ALLOYEI") == "LLY"
