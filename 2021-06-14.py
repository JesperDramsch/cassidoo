def printArrow(direction, length):
    """Print an arrow in direction and length the user provides

    Example:
        printArrow("left", 3)
        ...  *
        ... *
        ...*
        ... *
        ...  *

    Args:
        direction (str): Direction the arrow points "left" or "right"
        length (int): Length of arrow
    """
    print("Output:")

    if direction is "left":
        offset = 0
    elif direction is "right":
        offset = length
    else:
        raise

    for i in range(length * 2 - 1):
        print(" " * abs(offset - abs(1 + i - length)) + "*")


if __name__ == "__main__":
    printArrow("right", 3)

    printArrow("left", 5)

    printArrow("left", 4)
