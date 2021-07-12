from typing import Tuple


def binarize(num: int) -> Tuple[int]:
    """Generate Binary mask from CIDR

    Parameters
    ----------
    num : int
        CIDR

    Returns
    -------
    Tuple[int]
        Octets as base10 int of binary mask

    Examples
    --------
        >>> binarize(32)
        (255, 255, 255, 255)

        >>> binarize(23)
        (255, 255, 254, 0)
    """
    bin_mask = "1" * num + "0" * (32 - num)

    return tuple(int(bin_mask[i:i+8], base=2) for i in range(0, 32, 8))


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
    # Assume it's valid
    valid = True

    # Split IP and netmask into octets and CIRD block
    ip = tuple(int(octet) for octet in ip.split("."))
    netmask_base = tuple(int(octet) for octet in netmask.split("/")[0].split("."))
    cidr_block = binarize(int(netmask.split("/")[1]))

    # Iterate through octets and check range
    for ip_oct, netmask_oct, cidr_oct in zip(ip, netmask_base, cidr_block):
        if not netmask_oct <= int(ip_oct) <= (netmask_oct + 255 - cidr_oct):
            valid = False
            break

    return valid


if __name__ == "__main__":
    import doctest

    doctest.testmod()
