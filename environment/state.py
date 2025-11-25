
def get_state(self):
    snake_x, snake_y = self.snake_pos[0]
    green_x, green_y = get_closest(snake_x, snake_y, self.green_apples)

    moves = {
        'UP':    (snake_x, snake_y - 1),
        'DOWN':  (snake_x, snake_y + 1),
        'LEFT':  (snake_x - 1, snake_y),
        'RIGHT': (snake_x + 1, snake_y)
    }

    rewards = {}
    for dir, (x, y) in moves.items():
        reward = 0

        if x < 0 or x >= self.size or y < 0 or y >= self.size or (x, y) in self.snake_pos[1:]:
            reward = -3
        elif (dir == 'UP' and self.snake_dir == 'DOWN') or \
             (dir == 'DOWN' and self.snake_dir == 'UP') or \
             (dir == 'LEFT' and self.snake_dir == 'RIGHT') or \
             (dir == 'RIGHT' and self.snake_dir == 'LEFT'):
            reward = -1
        elif (x, y) in self.red_apples:
            reward = -2
        elif (x, y) in self.green_apples:
            reward = 1

        rewards[dir] = reward

    state = [snake_x, snake_y, green_x, green_y,
             rewards['UP'], rewards['DOWN'], rewards['LEFT'], rewards['RIGHT']]
    return state



def get_closest(snake_x, snake_y, obj):
    dist = []
    for (x, y) in obj:
        d = abs(snake_x - x) + abs(snake_y - y)
        dist.append((d, x, y))

    d, x, y = min(dist)
    return x, y
