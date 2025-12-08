"""
Visualization utilities for Snake RL model statistics.
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_eaten_apples(model_stats: dict) -> None:
    """
    Plot the average green and red apples eaten per model.
    """
    models = sorted(model_stats.keys())
    green_apples = [model_stats[m]['avg_green_apples'] for m in models]
    red_apples = [model_stats[m]['avg_red_apples'] for m in models]

    x = np.arange(len(models))
    width = 0.35

    plt.figure(figsize=(10, 6))
    plt.bar(x - width / 2, green_apples, width, label='Green Apples', color='green')
    plt.bar(x + width / 2, red_apples, width, label='Red Apples', color='red')

    plt.xticks(x, models)
    plt.xlabel("Model ID", fontsize=12)
    plt.ylabel("Apples", fontsize=12)
    plt.title("Apples eaten per Model", fontsize=14)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()


def plot_moves(model_stats: dict) -> None:
    """
    Plot the average number of moves per model.
    """
    models = sorted(model_stats.keys())
    moves = [model_stats[m]['avg_moves'] for m in models]

    plt.figure(figsize=(10, 6))
    plt.bar(models, moves)

    plt.xlabel("Model ID", fontsize=12)
    plt.ylabel("Moves", fontsize=12)
    plt.title("Moves per Model", fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()


def plot_snake_length(model_stats: dict) -> None:
    """
    Plot the average snake length per model.
    """
    models = sorted(model_stats.keys())
    snake_lens = [model_stats[m]['avg_snake_len'] for m in models]

    plt.figure(figsize=(10, 6))
    plt.bar(models, snake_lens)

    plt.xlabel("Model ID", fontsize=12)
    plt.ylabel("Snake Length", fontsize=12)
    plt.title("Snake Length per Model", fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()


def plot_stats(model_stats: dict) -> None:
    """
    Plot all relevant statistics per model, including snake length,
    moves, and apples eaten.
    """
    plot_snake_length(model_stats)
    plot_moves(model_stats)
    plot_eaten_apples(model_stats)
