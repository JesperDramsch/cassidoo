def isOdious(n: int) -> bool:
    """Find if a number is odious

    An “odious number” is a non-negative number that has an odd number of 1s
    in its binary expansion. Write a function that returns true if a given
    number is odious.

    Parameters
    ----------
    n : int
        Number to check for odiousness

    Returns
    -------
    bool
        Whether input is odious or not

    Example
    -------
        >>> isOdious(14)
        True

        >>> isOdious(5)
        False
    """

    # Check if the number is non-negative
    if n < 0:
        raise ValueError("Number is negative. Supply non-negative number.")

    # Nice little one-liner does:
    # 1. Convert to binary
    # 2. Count 1s
    # 3. Mod 2 to see if even or odd
    # 4. Convert to bool, because odd is 1 and True
    print(bool(f"{n:b}".count("1") % 2))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
