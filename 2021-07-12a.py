def binarize(ip: str) -> str:
    """Generate Binary mask from IP.

    Parameters
    ----------
    ip : str
        IPv4 as string

    Returns
    -------
    str
        Binary representation of IP

    Examples
    --------
        >>> binarize("192.168.4.0")
        '11000000101010000000010000000000'
    """

    return "".join(f"{int(octet):08b}" for octet in ip.split("."))


def inRange(ip: str, netmask: str) -> bool:
    """Test if IP is in range of Netmask (CIDR notation)

    Parameters
    ----------
    ip : str
        IPv4 address
    netmask : str
        IPv4 netmask with CIDR block

    Returns
    -------
    bool
        Response if IP is within netmask

    Examples
    --------
        >>> print(inRange("192.168.4.27", "192.168.0.0/16"))
        True
        >>> print(inRange("192.168.4.27", "192.168.1.0/24"))
        False
    """

    subnet, cidr = netmask.split("/")

    return binarize(ip)[: int(cidr)] == binarize(subnet)[: int(cidr)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
