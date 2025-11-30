
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


dangerous = ['W', 'S']
def distance_to_apple(view):
    for i, c in enumerate(view):
        if c == 'G':
            return i + 1
    return 0

def analyze_view(view):

    first = view[0]

    danger_first_step = 1 if first in dangerous else 0
    green_in_first_step = 1 if first == 'G' else 0
    red_in_first_step = 1 if first == 'R' else 0
    apple_in_path = 1 if 'G' in view else 0
    distance = distance_to_apple(view)

    # blocked_before_apple = 0
    # if apple_in_path:
    #     for c in view:
    #         if c == 'G':
    #             break
    #         if c in dangerous:
    #             blocked_before_apple = 1
    #             break

    return danger_first_step, green_in_first_step, red_in_first_step, apple_in_path, distance


def get_state(board):
    if not board.snake_pos:
        return
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
        d, g, r, a, d_a = analyze_view(v)
        features.extend([d, g, r, a, d_a])

    return tuple(features)

        

            