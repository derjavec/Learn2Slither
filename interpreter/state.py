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

dir_to_id = {
    'UP': 0,
    'RIGHT': 1,
    'DOWN': 2,
    'LEFT': 3,
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
def calculate_distance(size, view, x):
    for i, c in enumerate(view):
        if c == x:
            # return i + 1
            if i == 0:
                return 1
            elif i <= size // 3:
                return 2
            else:
                return 3
    return 0


def analyze_view(board, view):

    first  = view[0] if len(view) > 0 else 'W'
    second = view[1] if len(view) > 1 else 'W'
    third  = view[2] if len(view) > 2 else 'W'

    d1 = 1 if first in dangerous else 0
    d2 = 1 if second in dangerous else 0
    d3 = 1 if third in dangerous else 0

    dr = 1 if first == 'R' else 0
    dg = calculate_distance(board.size, view, 'G')

    cg = 0
    if dg != 0 and dg < board.last_min_dist:
        cg = 1

    return d1, d2, d3, dg, dr, cg


def get_state(board):
    if not board.snake_pos or board.done:
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
    abs_d = dir_to_id[board.snake_dir]
    for v in views:
        d1, d2, d3, dg, dr, cg= analyze_view(board, v)
        features.extend([d1, d2, d3, dg, dr, cg, abs_d])

    return tuple(features)

        

            