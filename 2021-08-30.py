from typing import List


def longestPrefix(data: List[str]) -> str:
    """Find the longest common prefix in a list of strings.

    Parameters
    ----------
    data : List[str]
        List with strings

    Returns
    -------
    str
        Longest prefix in list

    Examples
    --------
        >>> longestPrefix(["cranberry","crawfish","crap"])
        'cra'

        >>> longestPrefix(["parrot", "poodle", "fish"])
        ''
    """

    # Get number of items
    num_items = len(data)
    # Get shortest length of string
    min_string_length = min(map(len, data))

    # Iterate through each item and character position
    for i in range(min_string_length):
        for ii in range(1, num_items):
            # Check if character matches across items in list
            if data[0][i] != data[ii][i]:
                # Return slice of string on first failure
                return data[0][:i]
    # Default return of shortest string
    return data[0][:min_string_length]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
