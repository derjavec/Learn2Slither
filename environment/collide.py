from environment.reset import random_empty_cell

def game_over(self):
    if not self.snake_pos:
        self.done = True
        return        
    x, y = self.snake_pos[0]
    if x >= self.size or x < 0:
        self.done = True
    if y >= self.size or y < 0:
        self.done = True
    head = self.snake_pos[0]
    for tail in self.snake_pos[1:]:
        if head == tail:
            self.done = True
    

def eat_apples(self):

    for pos in self.red_apples:
        if pos == self.snake_pos[0]:
            self.red_apples.remove(pos)
            self.red_apples.append(random_empty_cell(self))
            self.eaten_red += 1           
            self.snake_pos.pop()
            if not self.snake_pos:
                return             
    for pos in self.green_apples:
        if pos == self.snake_pos[0]:
            self.eaten_green += 1
            self.green_apples.remove(pos)
            self.green_apples.append(random_empty_cell(self))
            x, y = self.snake_pos[-1]
            if self.snake_dir == 'UP':
                self.snake_pos.append((x, y + 1))
            if self.snake_dir == 'DOWN':
                self.snake_pos.append((x, y - 1))
            if self.snake_dir == 'RIGHT':
                self.snake_pos.append((x - 1, y))
            if self.snake_dir == 'LEFT':
                self.snake_pos.append((x + 1, y))