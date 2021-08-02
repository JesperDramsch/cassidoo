import numpy as np
from typing import List
from itertools import combinations


def check_semi_magic_square(square: np.array) -> bool:
    """Check if a square is a magic square (without diagonals)

    Parameters
    ----------
    square : np.array
        Array to be checked for semi_magic

    Returns
    -------
    bool
        Is it almost magical?
    """

    vert_sum = np.sum(square, 0)
    hori_sum = np.sum(square, 1)

    if np.all(vert_sum == vert_sum[0]) and np.all(hori_sum == vert_sum[0]):
        return True
    else:
        return False


def missingSevens(magic_square: List[List[int]]) -> int:
    """Replace numbers in square with 7 to find semi-magic square

    Parameters
    ----------
    magic_square : List[List[int]]
        Input square to be made magical

    Returns
    -------
    int
        Number of values to replace with 7 in square

    Example
    -------
        >>> missingSevens([[9,4,3],[3,4,9],[4,8,4]])
        0

        >>> missingSevens([[1,5,2],[5,9,5],[6,5,3]])
        4

        >>> missingSevens([[3,9,6],[8,5,5],[8,4,0]])
        2

    """

    # This calls for numpy. No way I'll do this by hand.
    magic_square = np.array(magic_square)

    # Check if it's already semi-magic
    if check_semi_magic_square(magic_square):
        return 0

    # Get the indexes in a neat pre-computed list
    locs = [x for x in range(magic_square.size)]

    # Iterate through numbers of replacements.
    for i in range(1, magic_square.size - min(magic_square.shape) + 1):
        # Use combinations of indexes
        for idx in combinations(locs, i):
            # copy the square
            square = magic_square.copy()
            # replace values with 7 at "combined" indices
            square[np.unravel_index(idx, magic_square.shape)] = 7
            # Check if that did the trick
            if check_semi_magic_square(square):
                return i
    # Replacing all square will always do the trick.
    return 9


if __name__ == "__main__":
    import doctest

    doctest.testmod()
