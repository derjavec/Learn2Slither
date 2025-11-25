

def move(self, action):
    opposites = {
        'UP': 'DOWN',
        'DOWN': 'UP',
        'LEFT': 'RIGHT',
        'RIGHT': 'LEFT'
    }
    if self.snake_dir is None: 
        self.snake_dir = action
        if action == 'RIGHT':
            self.snake_pos.reverse()
    x, y = self.snake_pos[0]
    if action != opposites[self.snake_dir]:
        if action == 'UP':
            new_head = (x  , y - 1)
        elif  action == 'DOWN':
            new_head = (x , y + 1)
        elif  action == 'RIGHT':
            new_head = (x + 1, y )
        elif  action == 'LEFT':
            new_head = (x - 1, y)
        self.snake_pos = [new_head] + self.snake_pos[:-1]
        self.snake_dir = action
        self.game_over()
        self.eat_apples()
    