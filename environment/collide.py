"""
Collision handling and apple consumption logic for the Snake environment.
"""

from environment.reset import random_empty_cell


def game_over(self) -> None:
    """
    Check if the game has ended due to collision with borders or itself.

    Sets `self.done = True` when:
    - Snake list is empty.
    - Snake head is outside the board.
    - Snake collides with its own body.
    """
    if not self.snake_pos:
        self.done = True
        return

    head_x, head_y = self.snake_pos[0]

    if head_x >= self.size or head_x < 0:
        self.done = True
    if head_y >= self.size or head_y < 0:
        self.done = True

    head = self.snake_pos[0]
    for segment in self.snake_pos[1:]:
        if head == segment:
            self.done = True
            break


def eat_apples(self) -> None:
    """
    Handle collisions between the snake's head and apples.

    - Green apples: increase snake length.
    - Red apples: decrease snake length. If reduced to zero, environment must
      handle termination upstream.
    """

    for pos in list(self.red_apples):
        if pos == self.snake_pos[0]:
            self.red_apples.remove(pos)
            self.red_apples.append(random_empty_cell(self))

            self.eaten_red += 1

            self.snake_pos.pop()

            if not self.snake_pos:
                return

    for pos in list(self.green_apples):
        if pos == self.snake_pos[0]:
            self.green_apples.remove(pos)
            self.green_apples.append(random_empty_cell(self))

            self.eaten_green += 1

            tail_x, tail_y = self.snake_pos[-1]

            if self.snake_dir == "UP":
                self.snake_pos.append((tail_x, tail_y + 1))
            elif self.snake_dir == "DOWN":
                self.snake_pos.append((tail_x, tail_y - 1))
            elif self.snake_dir == "RIGHT":
                self.snake_pos.append((tail_x - 1, tail_y))
            elif self.snake_dir == "LEFT":
                self.snake_pos.append((tail_x + 1, tail_y))
