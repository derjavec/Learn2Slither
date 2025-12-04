import matplotlib.pyplot as plt
import numpy as np


def plot_eaten_apples(model_stats):

    models = sorted(model_stats.keys())
    green_apples = [model_stats[m]['avg_green_apples'] for m in models]
    red_apples   = [model_stats[m]['avg_red_apples']   for m in models]

    x = np.arange(len(models))
    width = 0.35  # ancho de cada barra

    plt.figure(figsize=(10, 6))
    plt.bar(x - width/2, green_apples, width, label='Green Apples', color='green')
    plt.bar(x + width/2, red_apples,   width, label='Red Apples',  color='red')

    plt.xticks(x, models)
    plt.xlabel("Model ID", fontsize=12)
    plt.ylabel("Apples", fontsize=12)
    plt.title("Apples eaten per Model", fontsize=14)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()


def plot_movements(model_stats):

    models = sorted(model_stats.keys())
    movements = [model_stats[m]['avg_movements'] for m in models]

    plt.figure(figsize=(10, 6))
    plt.bar(models, movements)

    plt.xlabel("Model ID", fontsize=12)
    plt.ylabel("Movements", fontsize=12)
    plt.title("Movements per Model", fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()


def plot_snake_length(model_stats):

    models = sorted(model_stats.keys())
    q_table_lens = [model_stats[m]['avg_snake_len'] for m in models]

    plt.figure(figsize=(10, 6))
    plt.bar(models, q_table_lens)

    plt.xlabel("Model ID", fontsize=12)
    plt.ylabel("Snake length", fontsize=12)
    plt.title("Snake Length per Model", fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()


def plot_stats(model_stats):
    plot_snake_length(model_stats)
    plot_movements(model_stats)
    plot_eaten_apples(model_stats)