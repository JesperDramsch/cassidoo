from typing import List
from itertools import combinations_with_replacement


def distinctCombos(items: List[int], length: int) -> List[List[int]]:
    """Find the distinct combinations of an input list

    Given an integer array, find all distinct combinations of 
    a given length x (with repetition allowed).

    Parameters
    ----------
    items : List[int]
        List with items to combine
    length : int
        [description]

    Returns
    -------
    List[List[int]]
        Distinct combinations
    
    Examples
    --------
        >>> distinctCombos([1,1,2], 2)
        [[1, 1], [1, 2], [2, 2]]

        >>> distinctCombos([1,2,3,4], 2)
        [[1, 1], [1, 2], [1, 3], [1, 4], [2, 2], [2, 3], [2, 4], [3, 3], [3, 4], [4, 4]]
    """
    # Reduce to unique items
    distinct = list(set(items))

    # Find combinations of length, then turn into list of lists.
    return list(map(list, combinations_with_replacement(distinct, r=length)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()