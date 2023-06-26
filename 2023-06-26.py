from typing import List


def missingLetters(letters: List[str]) -> List[str]:
    """Find missing letters in consecutive list of letters

    Args:
        letters (List[str]): List of consecutive letters

    Returns:
        List[str]: Missing letters from list

    Examples:
        >>> missingLetters(['a','b','c','d','f'])
        ['e']

        >>> missingLetters(['a','b','c','d','e','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z'])
        ['f', 'g', 'v']

    """

    first = ord(letters[0])
    last = ord(letters[-1])

    pointer = 0
    missing = []

    for i in range(first, last):
        if i < ord(letters[pointer]):
            missing.append(chr(i))
        elif i > ord(letters[pointer]):
            raise ValueError("List must be consecutive")
        else:
            pointer += 1

    return missing


if __name__ == "__main__":
    import doctest

    doctest.testmod()
