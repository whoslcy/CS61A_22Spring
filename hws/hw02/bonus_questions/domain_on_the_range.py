# https://cs61a.org/exam/sp21/mt1/61a-sp21-mt1.pdf#page=14

def restrict_domain(f, low_d, high_d):
    """Returns a function that restrict the domain of F,
    a function that takes a single argument x.
    If x is not between LOW_D and HIGH_D (inclusive),
    it returns float("-inf"), but otherwise return F(x)
    >>> from math import sqrt
    >>> f = restrict_domain(sqrt, 1, 100)
    >>> f(25)
    5.0
    >>> f(-25)
    -inf
    >>> f(125)
    -inf
    >>> f(1)
    1.0
    >>> f(100)
    10.0
    """
    def wrapper_method_name(x):
        if low_d <= x and x <= high_d:
            return f(x)
        return float("-inf")
    return wrapper_method_name

def restrict_range(f, low_r, high_r):
    """Returns a function that restrict the range of F,
    a function that takes a single argument X.
    If the return value of F(X) is not between LOW_R and HIGH_R (inclusive),
    it returns -Infinity, but otherwise returns F(X).
    
    >>> cube = lambda x: x * x * x
    >>> f = restrict_range(cube, 1, 1000)
    >>> f(1)
    1
    >>> f(-5)
    -inf
    >>> f(5)
    125
    >>> f(10)
    1000
    >>> f(11)
    -inf
    """
    def wrapper_method_name(x):
        result = f(x)
        if low_r <= result and result <= high_r:
            return result
        return float("-inf")
    return wrapper_method_name

def restrict_both(f, low_d, high_d, low_r, high_r):
    """
    Returns a version of F with a domain restricted to [LOW_D, HIGH_D]
    and a range restricted to [LOW_R, HIGH_R].

    >>> diva = lambda x: (10000//x) * 9
    >>> f = restrict_both(diva, 1, 1000, 100, 999)
    >>> f(0)
    -inf
    >>> f(10000)
    -inf
    >>> f(200)
    450
    >>> f(100)
    900
    >>> f(1000)
    -inf
    """

    return restrict_range(restrict_domain(f, low_d, high_d), low_r, high_r)