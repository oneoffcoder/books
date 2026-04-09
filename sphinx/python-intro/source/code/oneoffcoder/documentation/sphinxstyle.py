def divide(a, b):
    """
    Divide one number by another.

    :param a: The numerator.
    :type a: float
    :param b: The denominator.
    :type b: float
    :return: The quotient ``a / b``.
    :rtype: float
    :raises ZeroDivisionError: If ``b`` is zero.
    """
    return a / b


print(divide(9.0, 3.0))
