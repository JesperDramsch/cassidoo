from typing import List
from collections import Counter


def wordle_guess(guess: str, solution: str) -> str:
    """Given a guess and a solution, return the wordle representation of the guess.

    Using the rules of Wordle, given a guess word and a solution word, 
    return a set of emojis returned from the guessWord.

    If the letter matches exactly in the position: 🟩
    If the letter is in the word but not in the correct position: 🟨
    If the letter is not in the word: ⬛

    Parameters
    ----------
    guess : str
        String with the guess
    solution : str
        String with the solution

    Returns
    -------
    str
        [description]

    Example
    -------

    >>> wordle_guess('reads', 'fudge')
    '⬛🟨⬛🟨⬛'

    >>> wordle_guess('lodge', 'fudge')
    '⬛⬛🟩🟩🟩'

    >>> wordle_guess('deeds', 'fudge')
    '🟨🟨⬛⬛⬛'

    """

    occurrences = Counter(solution)
    matches: List[str] = ["⬛"] * len(guess)

    # 🟩 🟨 ⬛
    for i, letter in enumerate(guess):
        if letter == solution[i]:
            matches[i] = "🟩"
        elif occurrences[letter] > 0:
            matches[i] = "🟨"
            occurrences[letter] -= 1

    return "".join(matches)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
