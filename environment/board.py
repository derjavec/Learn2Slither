import random


class Board:
    COLOR_RESET = "\033[0m"
    COLOR_SNAKE = "\033[34m"
    COLOR_GREEN_APPLE = "\033[32m"
    COLOR_RED_APPLE = "\033[31m"

    def __init__(self, size=10):
        self.go_flag = False
        self.size = size
        self.snake_pos = []
        self.snake_dir = None
        self.red_apples = []
        self.green_apples = []
        self.matrix = []
    
    
    def reset(self, snake_size = 3,green_apples_q = 2, red_apples_q = 1):
        self.snake_pos = self._place_snake(snake_size)
        self.green_apples = self._place_apples(green_apples_q)
        self.red_apples = self._place_apples(red_apples_q)
        self.update_matrix()


    def _place_snake(self, size=3):
        x = random.randint(0, self.size - size)
        y = random.randint(0, self.size - 1)
        self.snake_pos = [(x + i, y) for i in range(size)]
        return self.snake_pos

    
    def _place_apples(self, apples_q):
        return [self._random_empty_cell() for _ in range(apples_q)]
    

    def _random_empty_cell(self):
        while True:
            x = random.randint(0, self.size-1)
            y = random.randint(0, self.size-1)
            if (x,y) not in self.snake_pos + self.green_apples + self.red_apples:
                return (x,y)
    

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
            self.update_matrix()
    

    def game_over(self):
        x, y = self.snake_pos[0]
        if x >= self.size or x < 0:
            self.go_flag = True
        if y >= self.size or y < 0:
            self.go_flag = True
        head = self.snake_pos[0]
        for tail in self.snake_pos[1:]:
            if head == tail:
                self.go_flag = True
    

    def eat_apples(self):
        for pos in self.red_apples:
            if pos == self.snake_pos[0]:
                self.red_apples.remove(pos)
                self.red_apples.append(self._random_empty_cell())             
                self.snake_pos.pop()               
        for pos in self.green_apples:
            if pos == self.snake_pos[0]:
                self.green_apples.remove(pos)
                self.green_apples.append(self._random_empty_cell())
                x, y = self.snake_pos[-1]
                if self.snake_dir == 'UP':
                    self.snake_pos.append((x, y + 1))
                if self.snake_dir == 'DOWN':
                    self.snake_pos.append((x, y - 1))
                if self.snake_dir == 'RIGHT':
                    self.snake_pos.append((x - 1, y))
                if self.snake_dir == 'LEFT':
                    self.snake_pos.append((x + 1, y))

    
    def update_matrix(self):
        matrix = []
        for y in range(self.size):
            row = []
            for x in range(self.size):
                if (x, y) in self.snake_pos:
                    row.append('S')
                elif (x, y) in self.green_apples:
                    row.append('G')
                elif (x, y) in self.red_apples:
                    row.append('R')
                else:
                    row.append('0')
            matrix.append(row)
        self.matrix = matrix
    

    def print_board(self):
        for row in self.matrix:
            line = ""
            for cell in row:
                if cell == 'S':
                    line += f"{self.COLOR_SNAKE}S{self.COLOR_RESET} "
                elif cell == 'G':
                    line += f"{self.COLOR_GREEN_APPLE}G{self.COLOR_RESET} "
                elif cell == 'R':
                    line += f"{self.COLOR_RED_APPLE}R{self.COLOR_RESET} "
                else:
                    line += "0 "
            print(line)
