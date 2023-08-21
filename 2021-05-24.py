import curses
from itertools import groupby
from random import randint


class ConnectFour:
    def __init__(self, single=False, width=7, height=6) -> None:
        self.single_player = single
        self.height = height
        self.width = width
        self.board = [[" "] * height for _ in range(width)]
        self.player_one = input("Player One choose a Token: ")[0]
        self.player_two = (
            input("Player Two choose a Token: ")[0] if not self.single_player else "🤖"
        )
        self.player_one_turn = True
        self._won = False

    def board_state(self):
        """Returns a 2D version of the game state"""
        self.screen = curses.initscr()

        def _print_line(x, y):
            self.screen.addstr(y, x, "====" * self.width + "=")
            self.screen.refresh()

        _print_line(0, 0)
        for i in range(self.height - 1, -1, -1):
            self.screen.addstr(self.height - i, 0, "|" + "   |" * self.width)
            for ii in range(self.width):
                self.screen.addstr(self.height - i, 2 + 4 * ii, self.board[ii][i])
        _print_line(0, self.height + 1)

        self.screen.addstr(self.height + 2, 0, "|" + "   |" * self.width)
        for i in range(self.width):
            self.screen.addstr(self.height + 2, 2 + i * 4, str(i))
        _print_line(0, self.height + 3)

        if self._won:
            curses.napms(2000)
            curses.endwin()

    def has_won(self):
        """Return which player has won"""
        if self._won:
            return "Player One won" if self.player_one_turn else "Player Two won"

    def play(self):
        """Start the game!"""
        self._play = True
        while not self._won and self._play:
            self.turn()
            self.board_state()

    def _check_win(self, column, height):
        """Check if this turn won

        Args:
            column (int): column token was dropped
            height (int): height token was dropped
        """

        def winner(four) -> bool:
            for k, g in groupby(four):
                if len(tuple(g)) >= 4 and k != " ":
                    return True

        def threshold(val, thresh):
            return min(max(0, val), thresh - 1)

        # Check Vertical first
        vertical = self.board[column][max(0, height - 4) : height + 1]
        if winner(vertical):
            self._won = True
            return

        # Check Horizontal next
        horizontal = [
            self.board[col][height]
            for col in range(max(0, column - 3), min(column + 4, self.width))
        ]
        if winner(horizontal):
            self._won = True
            return

        # Check both diagonal lines
        diagonal_down = []
        diagonal_up = []
        for i in range(-3, 4):
            if (0 <= column + i < self.width) and (0 <= height + i < self.height):
                diagonal_down.append(self.board[column + i][height + i])
            if (0 <= column + i < self.width) and (0 <= height - i < self.height):
                diagonal_up.append(self.board[column + i][height - i])
        if winner(diagonal_down) or winner(diagonal_up):
            self._won = True
            return

    def which_column(self, y, x, prompt_string):
        curses.echo()
        self.screen.addstr(y, x, prompt_string)
        self.screen.addstr(y + 1, x, " " * 30)
        self.screen.refresh()
        inp = self.screen.getstr(y + 1, x, 20)

        # Enable exit
        if inp in (b"exit", b"quite", b"q", b"\x03"):
            self._play = False
            curses.endwin()
            return
        return int(inp)

    def turn(self):
        # Check if game is still on.
        if self._won:
            print("Game Over.")
            self.has_won()
            return

        # Get Valid input from current player
        player = "Player One" if self.player_one_turn else "Player Two"
        while True:
            if self.single_player and not self.player_one_turn:
                new_token = randint(0, self.width - 1)
                curses.napms(randint(0, self.width * 100))  # Thinking time
            else:
                new_token = self.which_column(
                    self.height + 5, 0, player + "! Choose a column: "
                )
            if not new_token:
                return
            elif self.board[new_token][-1] == " ":
                break
            else:
                self.screen.addstr(self.height + 6, 0, "Column Full!")
                self.screen.refresh()
                curses.napms(1000)

        # Fill Column
        position = self.board[new_token].index(" ")
        self.board[new_token][position] = (
            self.player_one if self.player_one_turn else self.player_two
        )

        # Check for win condition.
        self._check_win(new_token, position)

        # Win Condition end game!
        if self._won:
            win_text = ["Congratulations " + player + "!", "You won!"]
            for i, txt in enumerate(win_text):
                self.screen.addstr(
                    self.height // 2 + i, max(1, (4 * self.width - len(txt)) // 2), txt
                )
            self.screen.refresh()
            curses.napms(2500)
        # or Advance to next player
        else:
            self.player_one_turn = not self.player_one_turn


if __name__ == "__main__":
    board = ConnectFour(single=True)
    board.board_state()
    board.play()

    print(board.has_won())
