import pytest

from series import fib_recursive

@pytest.mark.parametrize("n, expected", [(0, 0), (1, 1), (2, 1), (10, 55)])

def test_fib_recursive(n, expected):
    result = fib_recursive(n)
    assert result == expected