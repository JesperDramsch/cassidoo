from datetime import date


def calculate_price(closing: str | date, visit: str | date, price: float, discount: float = 10) -> float:
    """Calculate price after discount per week.

    A store is going out of business and will reduce the price of all products by 10% every week leading up to the
    closing date. Given the closingDate, visitDate, and the originalPrice of a product, write a function that returns
    the price of the product on the visitDate. You can assume that originalPrice is a positive number.

    View: https://buttondown.com/cassidoo/archive/if-you-always-do-what-interests-you-at-least-one/

    Parameters
    ----------
    closing : str | date
        Closing date of store
    visit : str | date
        Visit date of customer
    price : float
        Price of the product
    discount : float, optional
        Percentage discount, by default 10

    Returns
    -------
    float
        Price after discount per week

    Examples
    --------
    >>> calculate_price('2025-04-01', '2025-03-03', 100)
    65.61

    >>> calculate_price('2025-04-01', '2025-03-15', 50)
    40.5

    >>> calculate_price('2025-04-01', '2025-04-15', 75)
    75.0
    """

    if isinstance(closing, str):
        closing = date.fromisoformat(closing)
    if isinstance(visit, str):
        visit = date.fromisoformat(visit)
    if discount >= 1:
        discount /= 100

    weeks = max(0, (closing - visit).days // 7)
    return price * (1 - discount) ** weeks


if __name__ == "__main__":
    import doctest

    doctest.testmod()
