
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

def look(self, direction):
    snake_x, snake_y = self.snake_pos[0]
    dx, dy = dir_to_delta[direction]
    x = snake_x
    y = snake_y
    one_dir = []
    while True:
        x += dx
        y += dy
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            one_dir.append('W')
            break
        c = self.matrix[y][x]
        one_dir.append(c)
        if c != '0':
            break
    return one_dir

def get_state(self):
    forward = self.snake_dir
    backward = opposites[forward]
    right = rights[forward]
    left = lefts[forward]
    state = [
        look(self, forward),
        look(self, left),
        look(self, right),
        look(self, backward)
    ]
    return state
        

            