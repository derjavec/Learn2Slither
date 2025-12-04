from environment.board import Board
from config.parser import get_config
from interpreter.state import get_state_training
from interpreter.action import direction_to_action
from agent.decision import take_decision_training
from agent.q_table import update_q_table
from utils.history import add_to_history
from utils.update_reward import penalize_repeted_states


def main():
    config = get_config()
    q_table = {}
    for episode in range(config['episodes']):
        board = Board(config['size'])
        board.reset(3, config['green_apples'], config['red_apples'])
        movements = 0
        while not board.done:
            movements += 1
            state = get_state_training(board)

            d = take_decision_training(q_table, state, config['e_greedy'], board.snake_dir)
            action = direction_to_action(board.snake_dir, d)

            board.step(action)
            
            new_state = get_state_training(board)
            reward = penalize_repeted_states(board, state)
            q_table = update_q_table(q_table, state, d, reward, new_state, config['alpha'], config['gamma'])
        
        print(f'episode {episode} snake length {len(board.snake_pos)} movements {movements}, q_table {len(q_table)}')
    add_to_history(config, q_table)

if __name__ == '__main__':
    main()