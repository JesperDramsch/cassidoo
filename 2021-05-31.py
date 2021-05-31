def inits(data):
    """ Return the prefixes of an iterable
        
    Given a list, 
    return a list of 
    all its prefixes 
    in ascending order of their length.

    Args:
        data (iterable): Iterable to return inits from

    Returns:
        list: List of Prefixes
    """
    return [data[:i] for i, _ in enumerate(data)] + [data]


if __name__ == "__main__":
    print(inits([4, 3, 2, 1]))

    print(inits([144]))

    print(inits("banana"))

