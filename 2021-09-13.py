from typing import List


def recur_parens(
    n: int,
    parens_list: List[str],
    parens: List[str] = None,
    pos: int = 0,
    open_parens: int = 0,
    close_parens: int = 0,
) -> List[str]:
    """Recursive function to generate well-formed parens pairs

    Parameters
    ----------
    n : int
        Number of parens pairs
    parens_list : List[str], optional
        List of well-formed parens pairs
    parens : List[str], optional
        List of individual parens, by default None
    pos : int, optional
        position in parens, by default 0
    open_parens : int, optional
        number of open parens in parens, by default 0
    close_parens : int, optional
        Number of closed parens in parens, by default 0

    Returns
    -------
    List[str]
        List of well-formed parens pairs as strings
    """

    # Open a new list of parens pairs with empty strings
    if parens is None:
        parens = [""] * 2 * n

    # We achieved balance if closed parens equal number of pairs
    if close_parens == n:
        # Join the parens list into a neat string and append to the list we pass in
        parens_list.append("".join(parens))
        return parens_list

    # Close last open parenthese
    if open_parens > close_parens:
        parens[pos] = ")"
        recur_parens(n, parens_list, parens, pos + 1, open_parens, close_parens + 1)

    # Open a new parens pair if we're below number of pairs n
    if open_parens < n:
        parens[pos] = "("
        recur_parens(n, parens_list, parens, pos + 1, open_parens + 1, close_parens)


def formParens(n: int) -> List[str]:
    """Generate well-formed parentheses

    Parameters
    ----------
    n : int
        Number of parens pairs

    Returns
    -------
    List[str]
        List of well-formed parens pairs

    Examples
    --------
        >>> formParens(1)
        ['()']

        >>> formParens(3)
        ['((()))', '(()())', '(())()', '()(())', '()()()']
    """

    # Pass in a list that we can fill
    y = []
    recur_parens(n, parens_list=y)

    # Sort so the tests pass. Not strictly necessary.
    return sorted(y)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
