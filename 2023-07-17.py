import re
from itertools import groupby
from typing import List


def explodeString(string: str) -> List[str]:
    """Explode a string into a list of sorted characters.

    Parameters
    ----------
    string : str
        String to explode.

    Returns
    -------
    List[str]
        Sorted list of characters

    Examples
    --------
    >>> explodeString('Ahh, abracadabra!')
    ['!', ',', 'A', 'aaaaa', 'bb', 'c', 'd', 'hh', 'rr']

    >>> explodeString('\\o/\\o/')
    ['//', '\\\\', 'oo']
    """
    return ["".join(list(g)).replace("\\\\", "\\") for k, g in groupby(sorted(re.sub(r"\s", "", string)))]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
