def sameDigits(num: int) -> bool:
    """Given an integer n, return true if n^3 and n have the same set of digits.

    Args:
        num (int): Number to test for equality

    Returns:
        bool: Whether cubed number has same set of digits
    """

    n = set(str(num))
    n_cube = set(str(num**3))
    return n == n_cube


if __name__ == "__main__":
    assert sameDigits(1)  # true
    assert sameDigits(10)  # true
    assert sameDigits(251894)  # true
    assert not sameDigits(251895)  # false
