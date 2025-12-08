"""
Movement logic for the Snake environment.
"""

opposites = {
    "UP": "DOWN",
    "DOWN": "UP",
    "LEFT": "RIGHT",
    "RIGHT": "LEFT",
}


def move(self, action: str) -> None:
    """
    Move the snake one step in the given direction.

    Prevents illegal 180° turns by ignoring moves in the opposite direction.
    Updates:
    - snake head position
    - snake body shift
    - snake direction
    Then triggers:
    - apple consumption
    - game over condition
    """
    if action == opposites[self.snake_dir]:
        return

    head_x, head_y = self.snake_pos[0]

    if action == "UP":
        new_head = (head_x, head_y - 1)
    elif action == "DOWN":
        new_head = (head_x, head_y + 1)
    elif action == "RIGHT":
        new_head = (head_x + 1, head_y)
    elif action == "LEFT":
        new_head = (head_x - 1, head_y)
    else:
        return

    self.snake_pos = [new_head] + self.snake_pos[:-1]
    self.snake_last_dir = self.snake_dir
    self.snake_dir = action

    self.eat_apples()
    self.game_over()
