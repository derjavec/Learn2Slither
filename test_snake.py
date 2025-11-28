from environment.board import Board
from interpreter.state import get_state
from interpreter.action import direction_to_action
from agent.decision import take_decision
from agent.q_table import update_q_table


board = Board(size=10)
board.reset()
q_table = {}
while not board.done:
    board.print_board()
    
    d = take_decision(board.state)

    action = direction_to_action(board.snake_dir, d)
    environment = board.step(action)
    state = get_state(environment)
    q_table = update_q_table(q_table, state, board.reward, 
    print(state)
print("GAME OVER!")
board.print_board()
