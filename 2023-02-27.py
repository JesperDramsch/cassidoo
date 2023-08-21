from typing import List


def repeatedGroups(numbers: List[int]) -> List[List[int]]:
    """Groups numbers in a list.

    Parameters
    ----------
    numbers : List[int]
        List of numbers to group

    Returns
    -------
    List[List[int]]
        Grouped Groups

    Examples
    --------
    >>> repeatedGroups([1, 2, 2, 4, 5])
    [[2, 2]]

    >>> repeatedGroups([1, 1, 0, 0, 8, 4, 4, 4, 3, 2, 1, 9, 9])
    [[1, 1], [0, 0], [4, 4, 4], [9, 9]]
    """
    current_num = numbers[0]
    count = 0
    out = []
    for num in numbers + [None]:
        if current_num != num:
            if count > 1:
                out.append([current_num] * count)
            count = 0
            current_num = num
        count += 1

    return out


if __name__ == "__main__":
    import doctest

    doctest.testmod()
