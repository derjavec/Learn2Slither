import random


class Board:


    def __init__(self, size=10):
        self.size = size
        self.snake_pos = []
        self.red_apples = []
        self.green_apples = []
        self.matrix = []
    
    
    def reset(self, snake_size = 3,green_apples_q = 2, red_apples_q = 1):
        self.snake_pos = self._place_snake(snake_size)
        self.green_apples = self._place_apples(green_apples_q)
        self.red_apples = self._place_apples(red_apples_q)
        self.update_matrix()


    def _place_snake(self, size = 3):
        x = random.randint(0, self.size - 1)
        y = random.randint(0, self.size - 3)
        self.snake_pos = [(x, y + i) for i in range(size)]
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
        x, y = self.snake_pos[0]
        if action == 'UP':
            new_head = (x  , y - 1)
        elif action == 'DOWN':
            new_head = (x , y + 1)
        elif action == 'RIGHT':
            new_head = (x + 1, y)
        elif action == 'LEFT':
            new_head = (x - 1, y)
        else:
            raise ValueError("Invalid action")
        self.snake_pos = [new_head] + self.snake_pos[:-1]
        self.update_matrix()
    

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
            print(row)
