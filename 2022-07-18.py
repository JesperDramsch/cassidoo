def hideEmail(email: str, hideFull: bool=False) -> str:
    """Hide an email address.
    
    Given a string that has a valid email address, write a function to hide the first part of the email (before the @ sign), minus the first and last character. 
    For extra credit, add a flag to hide the second part after the @ sign to your function excluding the first character and the domain extension.

    Parameters
    ----------
    email : str
        String with email to hide
    hideFull : bool, optional
        Flag to hide domain, by default False

    Returns
    -------
    str
        Hidden Email
    
    Examples
    --------
    >>> hideEmail('example@example.com')
    'e*****e@example.com'

    >>> hideEmail('example+test@example.co.uk', hideFull=True)
    'e**********t@e******.co.uk'

    >>> hideEmail('ex.am.ple+test@example.co.uk', hideFull=True)
    'e************t@e******.co.uk'
    """
    mid = email.index('@')

    first = email[0] + '*' * (mid - 2) + email[mid - 1] 

    if hideFull:
        tld = email[mid:].index('.')
        last = email[mid:mid + 2] + '*' * (tld - 2) + email[mid+tld:]
    else:
        last = email[mid:]

    return first + last


if __name__ == "__main__":
    import doctest

    doctest.testmod()
