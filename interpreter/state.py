"""
State representation and observation
analysis for the Snake RL environment.

Provides functions to extract features
from the board for training or inference.
"""

opposites = {
    "UP": "DOWN",
    "DOWN": "UP",
    "LEFT": "RIGHT",
    "RIGHT": "LEFT",
}

rights = {
    "UP": "RIGHT",
    "DOWN": "LEFT",
    "LEFT": "UP",
    "RIGHT": "DOWN",
}

lefts = {
    "UP": "LEFT",
    "DOWN": "RIGHT",
    "LEFT": "DOWN",
    "RIGHT": "UP",
}

dir_to_delta = {
    "UP": (0, -1),
    "DOWN": (0, 1),
    "LEFT": (-1, 0),
    "RIGHT": (1, 0),
}

dir_to_id = {
    "UP": 0,
    "RIGHT": 1,
    "DOWN": 2,
    "LEFT": 3,
}

dangerous = ["W", "S"]


def snake_view(board, direction):
    """
    Return the first non-empty cell in the
    given direction from the snake's head.

    Stops when hitting a wall, another snake
    segment, or an apple.
    """
    snake_x, snake_y = board.snake_pos[0]
    dx, dy = dir_to_delta[direction]
    x, y = snake_x, snake_y
    one_dir = []

    while True:
        x += dx
        y += dy
        if x < 0 or x >= board.size or y < 0 or y >= board.size:
            one_dir.append("W")
            break
        c = board.matrix[y][x]
        one_dir.append(c)
        if c != "0":
            break
    return one_dir


def calculate_distance(size, view, x):
    """
    Convert the distance to a cell of type `x` into a categorical distance.

    Categories:
    - 1: immediate
    - 2: near
    - 3: far
    - 0: not present
    """
    for i, c in enumerate(view):
        if c == x:
            if i == 0:
                return 1
            elif i <= 3:
                return 2
            else:
                return 3
    return 0


def analyze_view(board, view):
    """
    Convert a directional view into a feature vector.
    """

    dw = calculate_distance(board.size, view, "W")
    ds = calculate_distance(board.size, view, "S")
    dr = calculate_distance(board.size, view, "R")
    dg = calculate_distance(board.size, view, "G")

    return dw, ds, dg, dr


def get_state_training(board):
    """
    Return the feature tuple for training,
    including the count of visits to this state.
    """
    if not board.snake_pos or board.done:
        return

    forward = board.snake_dir
    left = lefts[forward]
    right = rights[forward]

    views = [
        snake_view(board, forward),
        snake_view(board, right),
        snake_view(board, left),
    ]

    features = []
    for v in views:
        dw, ds, dg, dr = analyze_view(board, v)
        features.extend([dw, ds, dg, dr])

    abs_d = dir_to_id[board.snake_dir]
    features.append(abs_d)

    abs_last_d = dir_to_id[board.snake_last_dir]
    features.append(abs_last_d)

    features = tuple(features)

    if features in board.visited_states:
        board.visited_states[features] += 1
    else:
        board.visited_states[features] = 0

    return features


def get_state(board):
    """
    Return the feature tuple for inference without updating visit count.
    """
    if not board.snake_pos or board.done:
        return

    forward = board.snake_dir
    left = lefts[forward]
    right = rights[forward]

    views = [
        snake_view(board, forward),
        snake_view(board, right),
        snake_view(board, left),
    ]

    features = []
    for v in views:
        dw, ds, dg, dr = analyze_view(board, v)
        features.extend([dw, ds, dg, dr])

    abs_d = dir_to_id[board.snake_dir]
    features.append(abs_d)

    abs_last_d = dir_to_id[board.snake_last_dir]
    features.append(abs_last_d)
 
    return tuple(features)
