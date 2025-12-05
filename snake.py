import argparse
import time
from environment.board import Board
from interpreter.state import get_state
from agent.decision import take_decision
from interpreter.action import direction_to_action
from utils.plots import plot_stats
from utils.history import load_models
from ui.visualizer import Visualizer


# -----------------------------------------------------------
# Run ONE testing session for ONE model
# -----------------------------------------------------------
def run_session(cfg, q_table, visual=False, step=False):
    board = Board(cfg["size"])
    board.reset(3, cfg["green_apples"], cfg["red_apples"])

    moves = 0
    visualizer = Visualizer(cfg["size"]) if visual else None

    while not board.done and moves < 500:
        state = get_state(board)

        decision = take_decision(q_table, state, board.snake_dir, cfg["size"])
        action = direction_to_action(board.snake_dir, decision)

        board.step(action)
        moves += 1

        if visual:
            visualizer.draw(board)
            if step:
                visualizer.wait_key()

    snake_len = len(board.snake_pos) + 1

    return {
        "snake_len": snake_len,
        "moves": moves,
        "green_apples": board.eaten_green,
        "red_apples": board.eaten_red
    }

def build_parser():
    parser = argparse.ArgumentParser(description="Run trained Slither model")
    parser.add_argument("--model_id", type=int)
    parser.add_argument("--sessions", type=int)
    parser.add_argument("--step_by_step", action="store_true", help="Run model step by step")
    parser.add_argument("--visual", action="store_true", help="Visualize board in terminal")
    return parser
# -----------------------------------------------------------
# MAIN
# -----------------------------------------------------------
def main():
    parser = build_parser()
    args = parser.parse_args()

    sessions = args.sessions if args.sessions else 1

    history = load_models(args.model_id)
    model_stats = {}

    for idx, model in enumerate(history):
        cfg = model["config"]
        q_table = model["q_table"]

        ep_results = []
        for s in range(sessions):
            result = run_session(
                cfg,
                q_table,
                visual=args.visual,
                step=args.step_by_step
            )
            ep_results.append(result)

            print(
                f"MODEL {idx} | session {s} | "
                f"len={result['snake_len']} moves={result['moves']} "
                f"G={result['green_apples']} R={result['red_apples']}"
            )

        model_stats[idx] = {
            "avg_snake_len": sum(e["snake_len"] for e in ep_results) / sessions,
            "avg_moves": sum(e["moves"] for e in ep_results) / sessions,
            "avg_green_apples": sum(e["green_apples"] for e in ep_results) / sessions,
            "avg_red_apples": sum(e["red_apples"] for e in ep_results) / sessions,
        }

        print("\n-----------------------------")
        print(f"MODEL {idx} SUMMARY")
        for k, v in model_stats[idx].items():
            print(f"{k}: {v}")
        print("-----------------------------\n")

    if len(model_stats) > 1:
        plot_stats(model_stats)


if __name__ == "__main__":
    main()
