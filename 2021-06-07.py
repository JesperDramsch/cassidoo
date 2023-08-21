from itertools import groupby


def lonely_number(*args):
    """Supply your numbers and get the product of the lonely numbers.

    Given three numbers, return their product.
    But, if one of the numbers is the same as another, it does not count:
    If two numbers are similar, return the lonely number.
    If all numbers are same, return 1.

    ♪♫ One is the loneliest number ♪♫

    Returns:
        int: The product of the lonely numbers
    """
    out = 1
    for number, group in groupby(args):
        if len(tuple(group)) == 1:
            out *= number
    return out


if __name__ == "__main__":
    print(lonely_number(1, 2, 3))

    print(lonely_number(6, 6, 4))

    print(lonely_number(7, 7, 7))  # Jackpot!
