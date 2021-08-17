def pSubstring(string: str) -> str:
    """Find the longest palindromic substring of input

    This approach iterates through center points in string and 
    grow palindromes out from the center point.

    Time complexity is O(n) I think (worst case is 1.5n), so it should be linear.
    Space complexity is constant O(1)

    Parameters
    ----------
    string : str
        Input string to search

    Returns
    -------
    str
        Palindromic string

    Example
    -------
        >>> pSubstring('babad')
        'bab'

        >>> pSubstring('malayalam')
        'malayalam'

        >>> pSubstring('blabla')
        'b'

        >>> pSubstring('qabbaqrtwcbbcwt')
        'twcbbcwt'
    """
    # Start on the left with length one
    substr_center, substr_len = 0, 1

    # Shift center point
    for center_point in range(1, str_len := len(string)):
        # Check if existing substring is longer than possible other substrings
        if substr_len > min(center_point, str_len - center_point) * 2:
            continue

        # Check even and odd palindromes around center point
        for even_odd in range(2):
            # Start left of centerpoint
            start = center_point - 1

            # Even starts on center point, odd starts right of center point
            end = center_point + even_odd

            # Iterate from center point check if "still" palindrome and within length
            while (start >= 0) and (end < str_len) and (string[start] == string[end]):
                start -= 1
                end += 1
            # Rewind to last palindrome before while fails
            else:
                start += 1
                end -= 1

            # Check if new substring is longer and save
            if (end - start + 1) > substr_len:
                substr_center = start
                substr_len = end - start + 1

    return string[substr_center : substr_center + substr_len]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
