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
    new_arr = arr.copy()
    for i in range(1, len(arr)):
        new_arr = [a + b for a, b in zip(arr[i:], new_arr)]
        out += new_arr.count(result)

    return out if out else -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
