from vecka5.uppgift32_lektion.pwstrength import compute_strength
import pytest


def test_pwlength():
    assert compute_strength("aaaaaaaaaaa") == compute_strength("aaaaaaaaaa") + 1


def test_to_short_pw():
    assert compute_strength("aaaaaaaaaa") == 0


def test_11_alpha():
    assert compute_strength("aaaaaaaaaaa") == 1


def test_symbols():
    assert compute_strength("#%&+_-") == 1


list_of_symbols = [("#", 1), ("%", 1), ("&", 1), ("+", 1), ("_", 1), ("-", 1),
                   ("a1", 1), ("aaaaaaaaaa1", 2), ("$", 0), ("asdkjf1h/", 0),
                   ("kasljdhfkasjhf%%1$", 0)]


@pytest.mark.parametrize("pw, st", list_of_symbols)
def test_pwstrength(pw, st):
    assert compute_strength(pw) == st

