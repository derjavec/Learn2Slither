from environment.board import Board
from config.parser import get_config
from interpreter.state import get_state_training
from interpreter.action import direction_to_action
from agent.decision import take_decision_training
from agent.q_table import update_q_table
from utils.history import add_to_history, load_models, rewrite_history_with_updates
from utils.update_reward import penalize_repeated_states


def init_q_table(add_sessions: int, model_id: int) -> dict:
    """
    Initialize the Q-table for a model.
    """
    if not add_sessions:
        return {}
    model = load_models(model_id)[0]
    return model["q_table"]


def run_sessions(q_table: dict, config: dict, n_sessions: int) -> dict:
    """
    Run multiple training sessions and update the Q-table.
    """
    for episode in range(n_sessions):
        board = Board(config['size'])
        board.reset(3, config['green_apples'], config['red_apples'])
        movements = 0

        while not board.done:
            movements += 1
            state = get_state_training(board)
            decision = take_decision_training(q_table, state, config['e_greedy'], board.snake_dir)
            action = direction_to_action(board.snake_dir, decision)
            board.step(action)
            new_state = get_state_training(board)

            reward = penalize_repeated_states(board, state)
            q_table = update_q_table(
                q_table, state, decision, reward, new_state,
                config['alpha'], config['gamma']
            )

        print(f"episode {episode} | snake len {len(board.snake_pos)} | moves {movements} | q_table {len(q_table)}")

    return q_table


def main():
    """
    Main function for running training sessions.

    - If add_sessions is None, runs new sessions and adds a new model to history.
    - If add_sessions is specified, adds sessions to existing model(s) and updates history.
    """
    add_sessions, model_id, config = get_config()

    if add_sessions is None:
        q_table = run_sessions({}, config, config['sessions'])
        add_to_history(config, q_table)
        return

    models = load_models(model_id)
    updated_models = []

    for m in models:
        print(f"Adding {add_sessions} sessions to model ID {m['id']}")
        q_new = run_sessions(m["q_table"], m["config"], add_sessions)
        updated_models.append({"id": m["id"], "config": m["config"], "q_table": q_new})

    rewrite_history_with_updates(updated_models, add_sessions)


if __name__ == '__main__':
    main()
