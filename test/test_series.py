import pytest

from fibonacci.series import fibonacci, lucas, sum_series

def test_fibonacci():
    assert fibonacci(1) == 0
    assert fibonacci(2) == 1
    assert fibonacci(5) == 3
    assert fibonacci(10) == 34
    with pytest.raises(ValueError):
        fibonacci(-1)

def test_lucas():
    assert lucas(1) == 2
    assert lucas(2) == 1
    assert lucas(5) == 7
    assert lucas(10) == 76
    with pytest.raises(ValueError):
        lucas(-1)
        

def test_sum_series():
    assert sum_series(5) == 3
    assert sum_series(10) == 34

    assert sum_series(5, 2, 1) == 7
    assert sum_series(10, 2, 1) == 76

    assert sum_series(5, 4, 2) == 14
    assert sum_series(10, 4, 2) == 230

    with pytest.raises(ValueError):
        sum_series(-1)



    