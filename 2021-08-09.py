from typing import List
from numpy import zeros


def generateMinesweeper(gridSize: int, mines: List[List[int]]) -> None:
    """Build a Minesweeper grid from mine locations

    Parameters
    ----------
    gridSize : int
        Size of square playing field
    mines : List[List[int]]
        List with mine coordinates (1-indexed)

    Examples
    --------
        >>> generateMinesweeper(5, [[1, 3], [3, 5], [2, 4]])
        xxxxx
        11xxx
        *21xx
        2*21x
        12*1x
    """
    # Open grid with zeros
    playing_field = zeros((gridSize, gridSize), dtype=int)

    # Validate mine input
    mines = tuple(
        filter(
            lambda coord: 0 < coord[0] <= gridSize and 0 < coord[1] <= gridSize, mines
        )
    )

    # Iterate over mines for adjacency +1
    for coord in mines:
        # Good ol' bounding boxes (input is 1-indexed)
        a1, a2 = max(coord[1] - 2, 0), min(coord[1] + 1, gridSize)
        b1, b2 = max(coord[0] - 2, 0), min(coord[0] + 1, gridSize)
        playing_field[a1:a2, b1:b2] += 1

    # Convert to string for shenanigans
    playing_field = playing_field.astype(str)

    # Iterate through mines to add mine location
    for coord in mines:
        playing_field[coord[1] - 1, coord[0] - 1] = "*"

    # Print each row and replace "0" with "x"
    for x in playing_field:
        print("".join(x).replace("0", "x"))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
