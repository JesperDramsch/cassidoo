def luhnCheck(number: int) -> bool:
    """Check if number is valid according to Luhn algorithm

    Parameters
    ----------
    number : int
        Card number candidate

    Returns
    -------
    bool
        Whether card is valid

    Examples
    --------
    >>> luhnCheck(123456789)
    False

    >>> luhnCheck(5555555555554444)
    True
    """

    number = str(number)
    number = list(map(int, number))
    number.reverse()

    for i in range(1, len(number), 2):
        number[i] *= 2
        if number[i] > 9:
            number[i] -= 9

    return sum(number) % 10 == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
