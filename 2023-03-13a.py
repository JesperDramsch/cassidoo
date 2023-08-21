import operator as op
from fractions import Fraction


def fractionMath(left: str, operator: str, right: str) -> str:
    w = Fraction(left)
    r = Fraction(right)

    ops = {
        "add": op.__add__,
        "subtract": op.__sub__,
        "multiply": op.__mul__,
        "divide": op.__itruediv__,
    }

    return str(ops[operator](w, r))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
