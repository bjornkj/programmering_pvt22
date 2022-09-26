import pytest
import uppgift_22


def test_square():
    assert uppgift_22.square(4) == 16


def test_circumference():
    assert uppgift_22.circumference(2) == pytest.approx(12.5664, 0.001)


def test_radius():
    assert uppgift_22.radius(12.5664) == pytest.approx(2, 0.001)


def test_factorial():
    assert uppgift_22.factorial(5) == 120


def test_factorial_0():
    assert uppgift_22.factorial(0) == 1
