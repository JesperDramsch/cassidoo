def numBalanced(parens: str) -> int:
    """Number of unbalanced parenthese.

    Given a string of parenthesis, return the number of parenthesis you need to add to the string in order for it to be balanced.

    Parameters
    ----------
    parens : str
        String with '(' and ')'

    Returns
    -------
    int
        Number of unbalanced parens

    Examples
    --------
    >>> numBalanced('()')
    0

    >>> numBalanced('(()')
    1

    >>> numBalanced('())(')
    2

    >>> numBalanced('))()))))()')
    6

    >>> numBalanced(')))))')
    5
    """
    left = 0
    residual = 0
    for p in parens:
        # Open
        if p == "(":
            left += 1
        # Close
        else:
            if left > 0:
                left -= 1
            else:
                residual += 1
    return residual + left


if __name__ == "__main__":
    import doctest

    doctest.testmod()
