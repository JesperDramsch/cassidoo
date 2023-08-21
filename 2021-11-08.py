from typing import List


def localPeaks(sequence: List[int]) -> List[int]:
    """Given an array of integers, return the index of each local peak.

    A “peak” element is an element that is greater than its neighbors.

    Parameters
    ----------
    sequence : List[int]
        List with integers to search for peaks

    Returns
    -------
    List[int]
        Index of peaks

    Example
    -------
        >>> localPeaks([1,2,3,1])
        [2]

        >>> localPeaks([1,3,2,3,5,6,4])
        [1, 5]

        >>> localPeaks([1,3,2,3,5,6])
        [1]
    """

    return [
        i
        for i, check in enumerate(sequence)
        if (sequence[max(0, i - 1)] < check)
        and (sequence[min(len(sequence) - 1, i + 1)] < check)
    ]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
