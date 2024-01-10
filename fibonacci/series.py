def fibonacci(n):
    """
    Calculate the nth number in the Fibonacci series using recursion.

    The Fibonacci series is a sequence of numbers where each number is the sum
    of the two preceding ones, usually starting with 0 and 1. This function 
    uses a recursive approach to calculate the Fibonacci number.

    Parameters:
    n (int): The position in the Fibonacci series to calculate. 
             The first position starts at 1.

    Returns:
    int: The nth Fibonacci number.

    Raises:
    ValueError: If n is not a positive integer.
    """
    if n <= 0:
        raise ValueError("no can do! n must be a positive integer")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2 )
    
def lucas(n):
    """
    Calculate the nth number in the Lucas series using recursion.

    The Lucas series is a sequence of numbers similar to the Fibonacci series,
    starting with 2 and 1. Each subsequent number is the sum of the two preceding ones.
    This function uses a recursive approach to calculate the Lucas number.

    Parameters:
    n (int): The position in the Lucas series to calculate. 
             The first position starts at 1.

    Returns:
    int: The nth Lucas number.

    Raises:
    ValueError: If n is not a positive integer.
    """
    if n <= 0:
        raise ValueError("no can do amigo! n must be a positive integer")
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n - 1) + lucas(n-2)
    
def sum_series(n, first=0, second=1):
    """
    Calculate the nth number in a series based on the sum of the two preceding numbers.

    This function is a generalization of the Fibonacci and Lucas series. 
    The series starts with two specified numbers and each subsequent number
    is the sum of the two preceding ones. By default, the function produces
    Fibonacci series numbers.

    Parameters:
    n (int): The position in the series to calculate. The first position starts at 1.
    first (int, optional): The first number in the series. Default is 0.
    second (int, optional): The second number in the series. Default is 1.

    Returns:
    int: The nth number in the series.

    Raises:
    ValueError: If n is not a positive integer.

    Examples:
    >>> sum_series(1)  # Fibonacci series
    0
    >>> sum_series(1, 2, 1)  # Lucas numbers
    2
    >>> sum_series(5, 4, 2)  # Custom series starting with 4 and 2
    14
    """
    if n <= 0:
        raise ValueError("No can do amigo! n must be a positive integer number")
    elif n == 1:
        return first
    elif n == 2:
        return second
    else:
        return sum_series(n - 1, first, second) + sum_series(n - 2, first, second)
    



