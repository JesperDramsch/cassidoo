import math


def simplify(numerator: int, denominator: int) -> str:
    """Simplify a fraction

    Parameters
    ----------
    numerator : int
        Number on top of fraction
    denominator: int
        Number on bottom of fraction

    Returns
    -------
    str
        Simplified fraction "1/2"

    Examples
    --------
    >>> simplify(2, 4)
    '1/2'

    >>> simplify(2, 1)
    '2'

    >>> simplify(8, 8)
    '1'
    """

    if numerator == denominator:
        return "1"

    divisor = math.gcd(numerator, denominator)

    numerator //= divisor
    denominator //= divisor

    if denominator == 1:
        out = f"{numerator}"
    elif numerator == 1:
        out = f"1/{denominator}"
    else:
        out = f"{numerator}/{denominator}"

    return out


def fractionMath(left, operator, right) -> str:
    """Combine two fractions and simplify the result

    Parameters
    ----------
    left : str
        String of fraction "2/3"
    operator : str
        Operation for fractions ("add", "subtract", "multiply", "divide")
    right : str
        String of fraction "2/3"

    Returns
    -------
    str
        Simplified result

    Examples
    --------
    >>> fractionMath("3/4", "add", "3/4")
    '3/2'

    >>> fractionMath("3/2", "subtract", "3/4")
    '3/4'

    >>> fractionMath("1/8", "multiply", "2/2")
    '1/8'

    >>> fractionMath("1/8", "divide", "2/2")
    '1/8'

    >>> fractionMath("1/7", "divide", "1/2")
    '2/7'

    >>> fractionMath("1/2", "add", "1/2")
    '1'
    """

    l_numerator, l_denominator = map(int, left.split("/"))
    r_numerator, r_denominator = map(int, right.split("/"))

    # Flip the right around for division into multiplication
    if operator == "divide":
        r_numerator, r_denominator = r_denominator, r_numerator
        operator = "multiply"

    # Don't have to find optimal extension, because we simplify at end
    l_numerator *= r_denominator
    r_numerator *= l_denominator
    new_denominator, l_denominator, r_denominator = (r_denominator * l_denominator,) * 3

    
    if operator == "add":
        new_numerator = l_numerator + r_numerator
    elif operator == "subtract":
        new_numerator = l_numerator - r_numerator
    elif operator == "multiply":
        new_numerator = l_numerator * r_numerator
        new_denominator = l_denominator * r_denominator

    fraction = simplify(new_numerator, new_denominator)

    return fraction


if __name__ == "__main__":
    import doctest

    doctest.testmod()
