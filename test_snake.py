from environment.board import Board
from interpreter.state import get_state
from interpreter.action import direction_to_action
from agent.decision import take_random_decision


board = Board(size=10)
board.reset()
while not board.done:
    board.print_board()
    d = take_random_decision(board.state)

    action = direction_to_action(board.snake_dir, d)
    environment = board.step(action)
    state = get_state(environment)

print("GAME OVER!")
board.print_board()
