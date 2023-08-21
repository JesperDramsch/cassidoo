from fractions import Fraction
import operator as op


def fractionMath(left: str, operator: str, right: str) -> str:

    l = Fraction(left)
    r = Fraction(right)

    ops = {
        "add": op.__add__,
        "subtract": op.__sub__,
        "multiply": op.__mul__,
        "divide": op.__itruediv__,
    }

    return str(ops[operator](l, r))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
