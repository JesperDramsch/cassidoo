def find_largest_interval(piano_keys: list[str]) -> int:
    """Find the largest interval between two consecutive keys.

    Write a function that takes a list of piano keys played in sequence and returns the largest interval
    (in semitones) between any two consecutive keys.
    Assume the lowest note is A0, and the highest is C8.

    This assumes piano key notation, where the keys are in the format of a capital letter followed by a number.
    The keys are in the format of a capital letter followed by a number. (e.g. 'A0', 'C1', 'G1', 'C2').

    View: https://buttondown.com/cassidoo/archive/if-youre-going-to-go-for-a-thing-theres-no-point/

    Parameters
    ----------
    piano_keys : list[str]
        List of piano keys

    Returns
    -------
    int
        Largest interval between two consecutive keys

    Examples
    --------
    >>> find_largest_interval(['A0', 'C1', 'G1', 'C2'])
    7

    >>> find_largest_interval(['C4', 'G4', 'C5', 'G3'])
    17

    >>> find_largest_interval(['E2', 'C3', 'G3', 'C8'])
    53
    """

    # Define the intervals between the keys, accounting for the C-major scale
    semitones = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}

    # Convert the keys to a list of tuples, where the first element is the number of semitones and the second element is the octave
    keys = [(semitones[key[0]], int(key[1])) for key in piano_keys]

    interval = 0

    for (f_tone, f_octave), (s_tone, s_octave) in zip(keys, keys[1:]):
        octaves = s_octave - f_octave
        tones = s_tone - f_tone

        # Octaves have 12 semitones and intervals can be "leftward" (e.g. C4 to B3)
        interval = max(interval, abs(octaves * 12 + tones))

    return interval


if __name__ == "__main__":
    import doctest

    doctest.testmod()
