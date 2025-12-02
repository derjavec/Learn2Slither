import argparse
import json
import os
from environment.board import Board
from interpreter.state import get_state
from agent.decision import take_decision
from interpreter.action import direction_to_action


def deserialize_keys(d):
    """Convierte claves string que representan tuplas en tuplas reales."""
    out = {}
    for k, v in d.items():
        if isinstance(k, str) and k.startswith("(") and k.endswith(")"):
            try:
                key = eval(k)  # porque las guardaste como str(tuple)
            except:
                key = k
        else:
            key = k

        if isinstance(v, dict):
            out[key] = deserialize_keys(v)
        else:
            out[key] = v

    return out


def load_model(model_id):
    path = "generated_files/history.json"
    if not os.path.exists(path):
        raise ValueError("No history.json found")

    with open(path, "r", encoding="utf-8") as f:
        all_histories = json.load(f)

    for item in all_histories:
        if "id" in item and item["id"] == model_id:
            config = item["config"]
            q_table = deserialize_keys(item["q_table"])
            model_history = item.get("model_history", {})
            return config, q_table, model_history

    raise ValueError(f"Model ID {model_id} not found")


def main():
    parser = argparse.ArgumentParser(description="Run trained Slither model")
    parser.add_argument("--model_id", type=int, required=True)
    args = parser.parse_args()

    config, q_table, model_history = load_model(args.model_id)

    board = Board(config['size'])
    board.reset(3, config['green_apples'], config['red_apples'])

    movements = 0

    while not board.done:
        board.print_board()

        movements += 1

        state = get_state(board)
        decision = take_decision(q_table, state, eps=0, snake_dir=board.snake_dir)
        action = direction_to_action(board.snake_dir, decision)

        board.step(action)


    print(f"snake length {len(board.snake_pos)} movements {movements}, q_table size {len(q_table)}")


if __name__ == "__main__":
    main()
