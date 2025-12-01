import random
from environment.reset import reset
from environment.move import move
from environment.collide import game_over, eat_apples
from environment.matrix import update_matrix, print_board
from environment.reward import calculate_reward


class Board:
    
    def __init__(self, size=10):
        self.done = False
        self.reward = 0
        self.size = size
        self.snake_pos = []
        self.snake_dir = 'LEFT'
        self.red_apples = []
        self.green_apples = []
        self.last_min_dist = size
        self.matrix = []
        self.state = []
    
    def step(self, action):
        self.calculate_reward(action)
        self.move(action)


    def calculate_reward(self, action):
        calculate_reward(self, action)
    
    
    def reset(self, snake_size = 3,green_apples_q = 2, red_apples_q = 1):
        reset(self, snake_size = 3, green_apples_q = 2, red_apples_q = 1)
        self.update_matrix()

    def move(self, action):
        move(self, action)
        self.update_matrix()
    

    def game_over(self):
        game_over(self)
    

    def eat_apples(self):
        eat_apples(self)


    def update_matrix(self):
        update_matrix(self)
    

    def print_board(self):
        print_board(self)
