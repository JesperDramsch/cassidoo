def longestPalindrome(string: str) -> str:
    """Find the longest palindrome with a wildcard string.

    Given a string s where some of the letters can
    be “wilds” (denoted by an underscore _), find the
    longest palindrome possible from the letters of s in
    order, where the wilds can be any character.

    This can rely heavily on the solution from 2021-08-17
    where we found the longest palindromic substring.

    This approach iterates through center points in string and
    grows palindromes out from the center point.

    Time complexity is O(n) I think (worst case is 1.5n), so it should be linear.
    Space complexity is constant O(1)

    Parameters
    ----------
    string : str
        String with wildcard to check for palindrome substring

    Returns
    -------
    str
        Longest Palindrome with wildcar replaced

    Examples
    --------
        >>> longestPalindrome('abcb_cbcbafg')
        'abcbccbcba'

        >>> longestPalindrome('xyzi_iizy')
        'yziiiizy'

        >>> longestPalindrome('otto')
        'otto'

        >>> longestPalindrome('o_tt_o')
        'oattao'

        >>> longestPalindrome('xyzi_ii_y')
        'yziiiizy'
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
            while (
                (start >= 0)
                and (end < str_len)
                and ((string[start] == string[end]) or (string[start] == "_") or (string[end] == "_"))
            ):
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

    # Get longest substring as list
    substring = [string[i] for i in range(substr_center, substr_center + substr_len)]

    # Iterate through Indices of list
    for i in range(substr_len):
        # Find wildcards
        if substring[i] == "_":
            # If opposite letter over centerpoint is also wildcard just use "a"
            if substring[substr_len - i - 1] == "_":
                substring[substr_len - i - 1] = "a"
            # Replace current wildcard with opposite letter over centerpoint
            substring[i] = substring[substr_len - i - 1]

    return "".join(substring)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
