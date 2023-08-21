def translateShift(shifted_text: str, shift: int = 1) -> str:
    """Translate a qwerty-cesars cipher.

    Args:
        shifted_text (str): Shifted Text to translate
        shift (int, optional): Shift the fingers are off on keyboard,
                               left is negative, right is positive. Defaults to 1.

    Returns:
        str: Unscambled text
    """

    buffer = [""] * abs(shift)
    qwerty_US = (
        buffer
        + ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "="]
        + buffer
        + [
            "q",
            "w",
            "e",
            "r",
            "t",
            "y",
            "u",
            "i",
            "o",
            "p",
            "[",
            "]",
            "\\",
        ]
        + buffer
        + [
            "a",
            "s",
            "d",
            "f",
            "g",
            "h",
            "j",
            "k",
            "l",
            ";",
            "'",
        ]
        + buffer
        + [
            "z",
            "x",
            "c",
            "v",
            "b",
            "n",
            "m",
            ",",
            ".",
            "/",
        ]
        + buffer
        + [
            " ",
            " ",
        ]
        + buffer
    )

    shift_l, shift_r = max(0, shift), max(0, -1 * shift)
    querty_shift = {a.upper(): b.upper() for a, b in zip(qwerty_US[shift_l:], qwerty_US[shift_r:])} | {
        a: b for a, b in zip(qwerty_US[shift_l:], qwerty_US[shift_r:])
    }

    return "".join(querty_shift[char] for char in shifted_text)


if __name__ == "__main__":
    print(translateShift(";p; epe"))
    # lol wow

    print(translateShift("vtsmnrttu"))
    # cranberry
