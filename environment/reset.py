import random

def reset(self, snake_size ,green_apples_q, red_apples_q):
    snake_size = int(snake_size)
    green_apples_q = int(green_apples_q)
    red_apples_q = int(red_apples_q)

    place_snake(self, snake_size)
    self.green_apples = place_apples(self, green_apples_q)
    self.red_apples = place_apples(self, red_apples_q)
    

def place_snake(self, snake_size):
    x = random.randint(0, self.size - snake_size)
    y = random.randint(0, self.size - 1)
    self.snake_pos = [(x + i, y) for i in range(snake_size)]

    
def place_apples(self, apples_q):
    return [random_empty_cell(self) for _ in range(apples_q)]


def random_empty_cell(self):
    while True:
        x = random.randint(0, self.size-1)
        y = random.randint(0, self.size-1)
        if (x,y) not in self.snake_pos + self.green_apples + self.red_apples:
            return (x,y)