import random
from typing import Optional


class NumberGuesser:
    def __init__(self, number: Optional[int] = None):
        if number is None:
            number = random.randint(1, 100)
        self.number = number

        self.guesses = 0

    def __repr__(self) -> str:
        return f"<NumberGuesser number={self.number} guesses={self.guesses}>"

    def guess(self, guess: int) -> bool:
        self.guesses += 1

        if guess == 69:
            print("Nice.", end=" ")

        if guess < self.number:
            print("Higher")
        elif guess > self.number:
            print("Lower")
        else:
            return True

        return guess == self.number

    def play(self) -> None:
        while True:
            guess = int(input("Guess a number: "))
            if self.guess(guess):
                print(f"Correct! It's {guess}. You won in {self.guesses} guesses!")
                break


if __name__ == "__main__":
    game = NumberGuesser()
    game.play()
