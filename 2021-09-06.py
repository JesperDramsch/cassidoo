from functools import singledispatch


@singledispatch
def convert_type(num):
    """Convert between str and int

    Parameters
    ----------
    num : str or int
        String or integer

    Returns
    -------
    int or str
        Str or integer number
    """
    raise NotImplementedError("Implement convert_type.")


@convert_type.register
def _(num: str) -> int:

    map_digits = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    # {str(a): a for a in range(10)}

    out = 0
    for i, digit in enumerate(num[::-1]):
        # Assign digit to location of power of 10
        out += 10 ** i * map_digits[digit]

    return out


@convert_type.register
def _(num: int) -> str:

    map_digits = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
    # {a: str(a) for a in range(10)}

    lst = []
    # Iterate through digits and convert them
    while num:
        lst.append(map_digits[num % 10])
        num //= 10

    return "".join(lst[::-1])


def stringProduct(*numbers_as_str: str) -> str:
    """Multiply any numbers provided as strings

    Given two non-negative integers n1 and n2 represented as strings, 
    return the product of n1 and n2, also represented as a string. 

    Twist: You can’t use any built-in language integer libraries nor convert the inputs to integers directly.

    Parameters
    ----------
    numbers_as_str : str
        Input numbers as strings.

    Returns
    -------
    str
        Product of input strings

    Examples
    --------
        >>> stringProduct("123", "456")
        '56088'
    """

    out = 1

    for num in numbers_as_str:
        out *= convert_type(num)

    return convert_type(out)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
