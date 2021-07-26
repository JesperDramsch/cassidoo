from math import log


def zerosEndingFactorial(factor: int) -> int:
    """Count the zeros ending a factorial

    The number of trailing zeros is dictated by the number of fives in the 
    prime factor decomposition of the factors. That's simply due to the fact
    that 2*5 = 10 and we have more than enough 2s and need matching 5s.
    If we wanted to decompose hundreds of numbers, we could go into cryptography 
    instead, so it's better to take the brute force approach:

    1. Figure out what the largest exponent of five is within the factorial.
    2. See how many times we can fit each exponential into the number.
    3. Sum it all up.

    Parameters
    ----------
    factor : int
        factor! to be counted

    Returns
    -------
    int
        Number of zeros at the end

    Examples
    --------
        >>> zerosEndingFactorial(1)
        0

        >>> zerosEndingFactorial(5)
        1

        >>> zerosEndingFactorial(100)
        24
    """

    # Find the largest exponential of 5 in factorial
    fives = int(log(factor, 5))

    # Obtain all counts
    zeros = [factor // 5 ** (i + 1) for i in range(fives)]

    # Sum all counts
    return sum(zeros)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
