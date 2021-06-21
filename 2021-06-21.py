from collections import deque


def gen_3D(length: int) -> deque:
    """Generate the 3D ASCII effect for drawCube

    Args:
        length (int): Length of cube

    Returns:
        deque: Queue of 3D shapes
    """

    num_chars = length // 2

    top = deque(" " * i + "|" for i in range(num_chars))

    mid = deque([" " * num_chars + "|"] * (num_chars + length % 2))
    mid.append(" " * num_chars + "+")

    bottom = deque(" " * (num_chars - i - 1) + "/" for i in range(num_chars))

    return top + mid + bottom


def drawCube(length: int) -> None:
    """Print a 3D ASCII cube with a length

    Args:
        length (int): Integer length of cube

    Examples:
        > drawCube(2)
          +----+
         /    /|
        +----+ |
        |    | +
        |    |/
        +----+

        > drawCube(3)
          +------+
         /      /|
        +------+ |
        |      | |
        |      | +
        |      |/
        +------+
    """

    h_length = 2 * length
    num_chars = length // 2

    # Prepare Components
    bar = "+" + "-" * h_length + "+"
    top = "/" + " " * h_length + "/"
    mid = "|" + " " * h_length + "|"
    d3d = gen_3D(length)

    # Print everything
    # Generate the top
    print(" " * (num_chars + 1) + bar)

    for i in range(num_chars):
        print(" " * (num_chars - i) + top + d3d.popleft())

    print(bar + d3d.popleft())

    # Generate bottom
    for _ in range(length):
        print(mid + d3d.popleft())

    print(bar)


if __name__ == "__main__":
    drawCube(1)

    drawCube(2)

    drawCube(3)

    drawCube(4)

    drawCube(5)
