

def move(self, action):

    x, y = self.snake_pos[0]
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
    self.eat_apples()
    self.game_over()
    