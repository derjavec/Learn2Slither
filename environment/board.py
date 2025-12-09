"""
Board environment wrapper for the Snake RL project.

This class delegates all core operations to the modules inside
`environment/`:
- reset()
- move()
- game_over()
- eat_apples()
- update_matrix()
- print_board()
- calculate_reward()

The Board class simply keeps the environment state and provides
a clean interface similar to OpenAI Gym's API.
"""

from environment.reset import reset
from environment.move import move
from environment.collide import game_over, eat_apples
from environment.matrix import update_matrix, print_board
from environment.reward import calculate_reward


class Board:
    """
    Snake game environment wrapper.
    """

    def __init__(self, size: int = 10):
        self.done = False
        self.reward = 0
        self.size = size

        self.snake_pos = []
        self.snake_dir = "LEFT"
        self.snake_last_dir = "LEFT"

        self.red_apples = []
        self.green_apples = []

        self.last_min_dist = size
        self.matrix = []

        self.visited_states = {}
        self.eaten_green = 0
        self.eaten_red = 0

    def step(self, action: str) -> None:
        """
        Execute one environment step.
        """
        self.calculate_reward(action)
        self.move(action)

    def reset(
        self,
        snake_size: int = 3,
        green_apples_q: int = 2,
        red_apples_q: int = 1,
    ) -> None:
        """
        Reset the environment to the initial state.
        """
        reset(
            self,
            snake_size=snake_size,
            green_apples_q=green_apples_q,
            red_apples_q=red_apples_q,
        )
        self.update_matrix()

    def calculate_reward(self, action: str) -> None:
        """Compute reward using external module."""
        calculate_reward(self, action)

    def move(self, action: str) -> None:
        """Move the snake and update the environment."""
        move(self, action)
        self.update_matrix()

    def game_over(self) -> None:
        """Update environment state when the snake dies."""
        game_over(self)

    def eat_apples(self) -> None:
        """Check and handle apple consumption."""
        eat_apples(self)

    def update_matrix(self) -> None:
        """Recompute the board matrix representation."""
        update_matrix(self)

    def print_board(self) -> None:
        """Print the board matrix (debugging only)."""
        print_board(self)
