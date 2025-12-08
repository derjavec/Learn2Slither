"""
Reward calculation logic for the Snake reinforcement learning environment.
"""

import math

dir_to_delta = {
    'UP': (0, -1),
    'DOWN': (0, 1),
    'LEFT': (-1, 0),
    'RIGHT': (1, 0),
}


def is_moving_towards_green(snake_x: int,
                            snake_y: int,
                            dx: int,
                            dy: int,
                            green_apples: list,
                            idx_closest: int) -> bool:
    """
    Return True if the movement direction leads toward the closest green apple.

    The check is axis-aligned since the snake moves on a grid.
    """
    gx, gy = green_apples[idx_closest]

    if dx != 0 and gy == snake_y:
        return (dx > 0 and gx > snake_x) or (dx < 0 and gx < snake_x)

    if dy != 0 and gx == snake_x:
        return (dy > 0 and gy > snake_y) or (dy < 0 and gy < snake_y)

    return False


def get_closest(x: int, y: int, green_apples: list) -> tuple:
    """
    Return (min_distance, index_of_closest_green_apple).
    """
    min_dist = float("inf")
    idx_closest = 0

    for i, (gx, gy) in enumerate(green_apples):
        dx = x - gx
        dy = y - gy
        d = math.sqrt(dx * dx + dy * dy)
        if d < min_dist:
            min_dist = d
            idx_closest = i

    return min_dist, idx_closest


def calculate_reward(self, action: str) -> None:
    """
    Compute the reward based on the next cell and the direction of movement.

    Rewards:
    - Wall:        -80
    - Self hit:   -100
    - Red apple:   -50
    - Green apple: +100
    - Moving closer toward green: +30
    """
    snake_x, snake_y = self.snake_pos[0]
    dx, dy = dir_to_delta[action]
    x = snake_x + dx
    y = snake_y + dy

    if x < 0 or y < 0 or x >= self.size or y >= self.size:
        cell = "W"
    else:
        cell = self.matrix[y][x]

    g, idx_closest = get_closest(x, y, self.green_apples)

    self.reward = 0

    if cell == "W":
        self.reward = -80
    if cell == "S":
        self.reward = -100
    elif cell == "R":
        self.reward = -50
    elif cell == "G":
        self.reward = 100
    elif is_moving_towards_green(
        snake_x, snake_y, dx, dy, self.green_apples, idx_closest
    ) and g < self.last_min_dist:
        self.reward = 30

    self.last_min_dist = g
