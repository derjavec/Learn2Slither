
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

def look(board, direction):
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


def get_state(board):
    
    if not board.snake_pos:
        return
    forward = board.snake_dir
    backward = opposites[forward]
    right = rights[forward]
    left = lefts[forward]
    state = [
        look(board, forward),
        look(board, right),
        look(board, backward),
        look(board, left)
    ]
    decoded_state = state_to_key(state)
    return decoded_state
        

            