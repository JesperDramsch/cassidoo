from collections import defaultdict
from itertools import combinations
from typing import List


def maxPointsOnLine(plane: List[List[int]]) -> int:
    """Count points in a line on a plane

    Args:
        plane (List[List[int, int]]): _description_

    Returns:
        int: Number of maximum points in a single line

    Examples:
        >>> maxPointsOnLine([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])
        4
    """
    tracker = defaultdict(list)
    for center, point in combinations(plane, 2):
        if point[0] == center[0]:
            slope = y_intercept = None
        else:
            slope = (point[1] - center[1]) / (point[0] - center[0])
            y_intercept = center[1] - slope * center[0]

        tracker[(y_intercept, slope)] += [tuple(center), tuple(point)]

    return max((len(set(v)) for v in tracker.values()), default=0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
