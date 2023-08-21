from typing import List


def reorder(values: List, index: List[int]) -> List:
    """Reorder list of values according index.

    Parameters
    ----------
    values : List
        List of values to sort
    index : List[int]
        Index to sort by

    Returns
    -------
    List
        Sorted values

    Example
    -------
        >>> reorder(["C", "D", "E", "F", "G", "H"], [3, 0, 4, 1, 2, 5])
        ['D', 'F', 'G', 'C', 'E', 'H']
    """
    # Check length match
    if len(values) != len(index):
        raise IndexError("Values and Index must be same length")

    # Open Array
    out = [False] * len(values)

    # Assign values to correct location
    for source, target in enumerate(index):
        out[target] = values[source]

    return out


if __name__ == "__main__":
    import doctest

    doctest.testmod()
