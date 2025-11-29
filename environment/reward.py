dir_to_delta = {
    'UP':    (0, -1),
    'DOWN':  (0, 1),
    'LEFT':  (-1, 0),
    'RIGHT': (1, 0)
}

def calculate_reward(self, action):
    snake_x, snake_y = self.snake_pos[0]
    dx, dy = dir_to_delta[action]
    x = snake_x + dx
    y = snake_y + dy
    if x >= self.size or y >= self.size or x < 0 or y < 0:
        c = 'W'
    else:
        c = self.matrix[y][x]
    if c == 'W' or c == 'S':
        self.reward = -3
    elif c == 'R':
        self.reward = -2
    elif c == 'G':
        self.reward = 2
    else:
        self.reward = 1
    
