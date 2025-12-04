import argparse
import json
import os
from environment.board import Board
from interpreter.state import get_state
from agent.decision import take_decision
from interpreter.action import direction_to_action
from utils.plots import plot_stats
from utils.history import load_models
import time


def main():
    parser = argparse.ArgumentParser(description="Run trained Slither model")
    parser.add_argument("--model_id", type=int)
    parser.add_argument("--episodes", type=int)
    args = parser.parse_args()

    history = load_models(args.model_id)
    episodes = args.episodes if args.episodes else  10

    model_stats = {}

    for idx, model in enumerate(history):
        cfg = model["config"]
        q_table = model["q_table"]

        ep_results = []

        for episode in range(episodes):
            movements = 0
            board = Board(cfg["size"])
            board.reset(3, cfg["green_apples"], cfg["red_apples"])
            start = time.time()
            eps = 0
            while not board.done:
                if movements > 0 :
                    if episodes == 1 or time.time() - start > 2:
                        board.print_board()
                        print(decision)
                        print('Q Table blocking:', q_table[state])
                    if time.time() - start > 2.5:
                        print('breaking the loop')
                        break
                state = get_state(board)
                decision = take_decision(q_table, state,  board.snake_dir, cfg["size"])
                action = direction_to_action(board.snake_dir, decision)
                movements += 1
                board.step(action)
            print(f'episode {episode} snake length {len(board.snake_pos) + 1} movements {movements}, q_table {len(q_table)}')
            ep_results.append({
                "snake_len": len(board.snake_pos) + 1,
                "movements": movements,
                "green_apples": board.eaten_green,
                "red_apples": board.eaten_red
            })

        avg_snake_len = sum(e["snake_len"] for e in ep_results) / episodes
        avg_movements = sum(e["movements"] for e in ep_results) / episodes
        avg_green = sum(e["green_apples"] for e in ep_results) / episodes
        avg_red = sum(e["red_apples"] for e in ep_results) / episodes

        model_stats[idx] = {
            "avg_snake_len": avg_snake_len,
            "avg_movements": avg_movements,
            "avg_green_apples": avg_green,
            "avg_red_apples": avg_red
        }

        print(f"\nMODEL {idx}")
        print(f"Avg snake length: {avg_snake_len}")
        print(f"Avg movements: {avg_movements}")
        print(f"Avg green apples: {avg_green}")
        print(f"Avg red apples: {avg_red}")

    if episodes > 1:
        plot_stats(model_stats)



if __name__ == "__main__":
    main()
