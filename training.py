from environment.board import Board
from config.parser import get_config
from interpreter.state import get_state
from interpreter.action import direction_to_action
from agent.decision import take_decision
from agent.q_table import update_q_table



def main():
    config = get_config()
    q_table = {}
    for episode in range(config['episodes']):
        board = Board(config['size'])
        board.reset(3, config['green_apples'], config['red_apples'])
        movements = 0
        while not board.done:
            # board.print_board()

            movements += 1
            state = get_state(board)
            d = take_decision(q_table, state, config['e_greedy'], board.snake_dir)
            action = direction_to_action(board.snake_dir, d)
            # print(action)
            # print(f'snake_dir {board.snake_dir}, decision {d}, action {action}, reward {board.reward}')
            board.step(action)
            # print('reward ',board.reward)
            new_state = get_state(board)
            q_table = update_q_table(q_table, state, d, board.reward, new_state, config['alpha'], config['gamma'])
            # print('q table ',q_table)
        print(f'episode {episode} snake length {len(board.snake_pos)} movements {movements}, q_table {len(q_table)}')
    
    




if __name__ == '__main__':
    main()