"""
Matrix generation and board rendering for the Snake environment.
"""

COLOR_RESET = "\033[0m"
COLOR_SNAKE = "\033[34m"
COLOR_SNAKE_HEAD = "\033[33m"
COLOR_GREEN_APPLE = "\033[32m"
COLOR_RED_APPLE = "\033[31m"


def update_matrix(self) -> None:
    """
    Build the board matrix based on the current snake and apples.

    Fills `self.matrix` with:
    - 'S' for snake segments
    - 'G' for green apples
    - 'R' for red apples
    - '0' for empty cells
    """
    matrix = []

    for y in range(self.size):
        row = []
        for x in range(self.size):
            pos = (x, y)
            if self.snake_pos and pos == self.snake_pos[0]:
                row.append("H")
            elif pos in self.snake_pos:
                row.append("S")
            elif pos in self.green_apples:
                row.append("G")
            elif pos in self.red_apples:
                row.append("R")
            else:
                row.append("0")
        matrix.append(row)

    self.matrix = matrix


def print_board(self) -> None:
    """
    Print the board matrix using ANSI colors for debugging.

    - Snake = blue
    - Green apple = green
    - Red apple = red
    """
    for row in self.matrix:
        line = ""
        for cell in row:
            if cell == "H":
                line += f"{COLOR_SNAKE_HEAD}H{COLOR_RESET} "
            elif cell == "S":
                line += f"{COLOR_SNAKE}S{COLOR_RESET} "
            elif cell == "G":
                line += f"{COLOR_GREEN_APPLE}G{COLOR_RESET} "
            elif cell == "R":
                line += f"{COLOR_RED_APPLE}R{COLOR_RESET} "
            else:
                line += "0 "
        print(line)
