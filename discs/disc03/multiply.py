def multiply(m, n):
    """
    Takes two positive integers and returns their productr using recursion.

    >>> multiply(5, 3)
    15
    """
    "***YOUR CODE HERE***"
    if n == 1:
        return m
    else:
        return m + multiply(m, n-1)