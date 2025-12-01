import math

dir_to_delta = {
    'UP':    (0, -1),
    'DOWN':  (0, 1),
    'LEFT':  (-1, 0),
    'RIGHT': (1, 0)
}


def is_moving_towards_green(snake_x, snake_y, dx, dy, green_apples):

    for gx, gy in green_apples:
        if dx != 0 and gy == snake_y:
            if (dx > 0 and gx > snake_x) or (dx < 0 and gx < snake_x):
                return True
        elif dy != 0 and gx == snake_x:
            if (dy > 0 and gy > snake_y) or (dy < 0 and gy < snake_y):
                return True
    return False

def get_closest(x, y, green_apples): 
    min_dist = float('inf') 
    for gx, gy in green_apples: 
        dx = x - gx 
        dy = y - gy 
        d = math.sqrt(dx**2 + dy**2) 
        if d < min_dist: 
            min_dist = d 
    return min_dist


def calculate_reward(self, action):
    snake_x, snake_y = self.snake_pos[0]
    dx, dy = dir_to_delta[action]
    x = snake_x + dx
    y = snake_y + dy

    if x < 0 or y < 0 or x >= self.size or y >= self.size:
        c = 'W'
    else:
        c = self.matrix[y][x]

    g = get_closest(x, y, self.green_apples)

    self.reward = 0.1

    if c == 'W' or c == 'S':
        self.reward = -100
    elif c == 'R':
        self.reward = -30
    elif c == 'G':
        self.reward = 100
    elif is_moving_towards_green(snake_x, snake_y, dx, dy, self.green_apples) and g < self.last_min_dist:
        self.reward = 50

    self.last_min_dist = g

    


    
