import argparse
from environment.board import Board
from interpreter.state import get_state
from agent.decision import take_decision
from interpreter.action import direction_to_action
from utils.plots import plot_stats
from utils.history import load_models
from ui.visualizer import Visualizer


def run_session(cfg: dict, q_table: dict, visual: bool = False, step: bool = False) -> dict:
    """
    Run one testing session for a single model.
    """
    board = Board(cfg["size"])
    board.reset(3, cfg["green_apples"], cfg["red_apples"])
    moves = 0
    visualizer = Visualizer(cfg["size"]) if visual else None

    while not board.done and moves < 500:
        # board.print_board()
        state = get_state(board)
        decision = take_decision(q_table, state, board.snake_dir, cfg["size"])
        # print(decision)
        action = direction_to_action(board.snake_dir, decision)
        board.step(action)
        moves += 1

        if visual:          
            # print(state, q_table.get(state, [0, 0, 0]))
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


def run_model_sessions(model: dict, sessions: int, visual: bool, step: bool) -> dict:
    """
    Run multiple sessions for a single model and collect averaged statistics.
    """
    cfg = model["config"]
    q_table = model["q_table"]
    ep_results = []

    for s in range(sessions):
        result = run_session(cfg, q_table, visual=visual, step=step)
        ep_results.append(result)
        print(
            f"Session {s} | len={result['snake_len']} moves={result['moves']} "
            f"G={result['green_apples']} R={result['red_apples']}"
        )

    stats = {
        "avg_snake_len": sum(e["snake_len"] for e in ep_results) / sessions,
        "avg_moves": sum(e["moves"] for e in ep_results) / sessions,
        "avg_green_apples": sum(e["green_apples"] for e in ep_results) / sessions,
        "avg_red_apples": sum(e["red_apples"] for e in ep_results) / sessions,
    }

    return stats


def build_parser() -> argparse.ArgumentParser:
    """
    Build the command-line argument parser.
    """
    parser = argparse.ArgumentParser(description="Run trained Slither model")
    parser.add_argument("--model_id", type=int, help="Specify the ID of the model to run")
    parser.add_argument("--sessions", type=int, help="Number of sessions to run per model")
    parser.add_argument("--step_by_step", action="store_true", help="Run model step by step")
    parser.add_argument("--visual", action="store_true", help="Visualize board in terminal")
    return parser


def main():
    """
    Main function to run one or multiple trained Slither models, collect statistics, 
    and optionally visualize the sessions.
    """
    parser = build_parser()
    args = parser.parse_args()
    sessions = args.sessions if args.sessions else 1

    history = load_models(args.model_id)
    model_stats = {}

    for idx, model in enumerate(history):
        print(f"\n--- Running Model {idx} ---")
        stats = run_model_sessions(model, sessions, args.visual, args.step_by_step)
        model_stats[idx] = stats

        print(f"\nMODEL {idx} SUMMARY")
        for k, v in stats.items():
            print(f"{k}: {v}")
        print("-----------------------------\n")

    if len(model_stats) > 1:
        plot_stats(model_stats)


if __name__ == "__main__":
    main()
