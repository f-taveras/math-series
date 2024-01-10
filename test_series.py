import pytest

from series import fibonacci

def test_base():
    assert fibonacci(1) == 0

def test_second():
    assert fibonacci(2) == 1 

def test_third():
    assert fibonacci(3) == 1

def test_fifth():
    assert fibonacci(5) == 3


def test_invalid_input():
    assert fibonacci(0) == "no can do! n must be a positive integer"
    assert fibonacci(-1) == "no can do! n must be a positive integer"



    