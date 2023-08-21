from typing import List


def subarraySum(arr: List[int], result: int) -> int:
    """Count the subarrays that result in predicted number

    Parameters
    ----------
    arr : List[int]
        Array to check
    result : int
        Result subarrays sum to

    Returns
    -------
    int
        Number of subarrays that sum to result

    Example
    -------
        >>> subarraySum([10 , 2, -2, -20, 10], -10)
        3
        >>> subarraySum([10 , 2, -2, -20, 10], 999)
        -1
        >>> subarraySum([10 , 2, -2, -20, 10], 0)
        2
    """
    out = arr.count(result)
    sum_tracker = arr.copy()

    # Shift start for loop 2
    for i in range(1, len(arr)):
        # Go through tail arrays from shifted start
        for ii, a in enumerate(arr[i:]):
            sum_tracker[ii] += a
            out += sum_tracker[ii] == result

    return out or -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
