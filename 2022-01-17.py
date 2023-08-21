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

    >>> wordle_guess('error', 'tries')
    '🟨🟩⬛⬛⬛'

    >>> wordle_guess('cooks', 'blond')
    '⬛⬛🟩⬛⬛'

    >>> wordle_guess('abbbb', 'aaccc')
    '🟩⬛⬛⬛⬛'
    """
    # Generate list with all misses as default
    matches: List[str] = ["⬛"] * len(guess)

    # Get counts of letters in the solution
    occurrences = Counter(solution)

    # Prepare dictionary for sparse misplaced letters
    misplaced_candidate = {}

    # 🟩 ⬛ Handle exact matches and misses
    for i, letter in enumerate(guess):
        # Exact match
        if letter == solution[i]:
            matches[i] = "🟩"
            occurrences[letter] -= 1
        # Not misses, so candidate for misplaced
        elif occurrences[letter] > 0:
            misplaced_candidate[i] = letter

    # 🟨 Handle possibly misplaced letters
    for i, letter in misplaced_candidate.items():
        if occurrences[letter] > 0:
            matches[i] = "🟨"
            occurrences[letter] -= 1

    return "".join(matches)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(wordle_guess("irate", "frame"))
    print(wordle_guess("later", "frame"))
    print(wordle_guess("soare", "frame"))
    print(wordle_guess("roate", "frame"))
    print(wordle_guess("crane", "frame"))
