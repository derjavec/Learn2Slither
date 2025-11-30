
opposites = {
    'UP': 'DOWN',
    'DOWN': 'UP',
    'LEFT': 'RIGHT',
    'RIGHT': 'LEFT'
}
rights = {
    'UP': 'RIGHT',
    'DOWN': 'LEFT',
    'LEFT': 'UP',
    'RIGHT': 'DOWN'
}
lefts = {
    'UP': 'LEFT',
    'DOWN': 'RIGHT',
    'LEFT': 'DOWN',
    'RIGHT': 'UP'
}

dir_to_delta = {
    'UP':    (0, -1),
    'DOWN':  (0, 1),
    'LEFT':  (-1, 0),
    'RIGHT': (1, 0)
}

def snake_view(board, direction):
    snake_x, snake_y = board.snake_pos[0]
    dx, dy = dir_to_delta[direction]
    x = snake_x
    y = snake_y
    one_dir = []
    while True:
        x += dx
        y += dy
        if x < 0 or x >= board.size or y < 0 or y >= board.size:
            one_dir.append('W')
            break
        c = board.matrix[y][x]
        one_dir.append(c)
        if c != '0':
            break
    return one_dir


def state_to_key(state):
    return tuple(tuple(row) for row in state)

dangerous = ['W', 'S', 'R']

def analyze_view(view):

    first = view[0]

    danger_first_step = 1 if first in dangerous else 0

    apple_in_path = 1 if 'G' in view else 0

    blocked_before_apple = 0
    if apple_in_path:
        for c in view:
            if c == 'G':
                break
            if c in dangerous:
                blocked_before_apple = 1
                break

    return danger_first_step, apple_in_path, blocked_before_apple


def get_state(board):
    forward = board.snake_dir
    left = lefts[forward]
    right = rights[forward]

    views = [
        snake_view(board, forward),
        snake_view(board, right),
        snake_view(board, left)
    ]

    features = []

    for v in views:
        d, a, b = analyze_view(v)
        features.extend([d, a, b])

    return tuple(features)

        

            