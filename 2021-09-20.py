import re


def parseHTML(html: str):
    """Generate list from raw html

    Parameters
    ----------
    html : str
        HTML to parse

    Returns
    -------
        List of List (of List?) with Tags and attributes parsed

    Example
    -------
        >>> parseHTML('<p><img src="https://i.imgur.com/LSG9xg3.jpeg" /></p>')
        [{'tag': 'p'}, {'tag': 'img', 'attributes': [{'src': 'https://i.imgur.com/LSG9xg3.jpeg'}]}]
    """
    out = []

    # Use Regex to get all HTML tags that aren't closing tags
    for snippet in re.findall(r"(?<=<)[^/].*?(?=\s?/?>)", html):
        processed = {}

        # Split the snippet into tag and attributes
        snippet = snippet.split(" ")

        # Get the tag, there's always a tag, remove it from list
        processed["tag"] = snippet.pop(0)

        # The remaining data in the snippet is attributes (if any)
        attrs = []
        for attribute in snippet:
            name, value = attribute.split("=")
            attrs.append({name: value.replace('"', "").replace("'", "")})

        # If there were attributes, attrs is filled, otherwise this is skipped
        if attrs:
            processed["attributes"] = attrs

        # Append it to our output list
        out.append(processed)

    return out


if __name__ == "__main__":
    import doctest

    doctest.testmod()
