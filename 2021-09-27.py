from typing import List


def eval_and_or_xor(one: bool, op: str, two: bool) -> bool:
    """Evaluate three components with using 'eval()'

    Parameters
    ----------
    one : bool
        First boolean
    op : str
        Operator as string, [&, |, ^]
    two : bool
        Second Boolean

    Returns
    -------
    bool
        Result of boolean operation
    """

    if op == "^":
        return one != two
    elif op == "|":
        return one or two
    elif op == "&":
        return one and two


def recur_eval(components: List, results: List, pointer: int = 0) -> List[bool]:
    """Recurring evaluation of parantheses combinations

    Parameters
    ----------
    components : List
        True, False, and booleans
    results : List
        List for results
    pointer : int, optional
        Start point in list for evaluation, by default 0

    Returns
    -------
    List[bool]
        List with results from evaluations
    """

    # End result of all combinations, when 1 item is left
    if len(components) == 1:
        results.append(components[0])
        return

    # Start from left of components
    for i in range(pointer, len(components) - 2, 2):
        # Prepend all components before pointer
        reduced = components[:i]
        # Iterate through expressions right of pointer
        for ii in range(i, len(components) - 2, 4):
            # Combine current expression pair
            combined = eval_and_or_xor(
                components[ii], components[ii + 1], components[ii + 2]
            )
            # Make the print kinda nice
            # print(ii, i, "{", components[ii], components[ii+1], components[ii+2], "\t} = ", combined)

            # Append the combined result to existing components
            reduced.append(combined)

            # Pass to next evaluation
            # The components get the unprocessed components that are left
            # The pointer is either zero or two left of the current pointer
            recur_eval(reduced + components[ii + 3 :], results, max(0, i - 2))


def evaluateExp(expression: str) -> int:
    """Evaluate all parentheses for a given expression

    Given a string expression with the symbols T for true,
    F for false, & for AND, | for OR, and ^ for XOR, count
    the number of ways we can parenthesize the expression so
    that its value evaluates to true.

    Parameters
    ----------
    expression : str
        Expression of T, F, |, &, ^

    Returns
    -------
    int
        Number of true expressions

    Example
    -------
        >>> evaluateExp('T|T')
        1
        >>> evaluateExp('T|T&F^T')
        4
        >>> evaluateExp('T|T&F^T&T')
        12
    """

    # Process input
    components = []
    for char in expression:
        if char == "F":
            components.append(False)
        elif char == "T":
            components.append(True)
        else:
            components.append(char)

    # Instantiate a list for the recurring results
    results = []
    recur_eval(components, results)

    # Sum the booleans
    return sum(results)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
