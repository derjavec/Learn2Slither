import matplotlib.pyplot as plt


def plot_red_apples(model_stats):

    models = sorted(model_stats.keys())
    red_apples = [model_stats[m]['avg_red_apples'] for m in models]

    plt.figure(figsize=(10, 6))
    plt.bar(models, red_apples)

    plt.xlabel("Model ID", fontsize=12)
    plt.ylabel("Red Apples", fontsize=12)
    plt.title("Red Apples eaten per Model", fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()


def plot_green_apples(model_stats):

    models = sorted(model_stats.keys())
    green_apples = [model_stats[m]['avg_green_apples'] for m in models]

    plt.figure(figsize=(10, 6))
    plt.bar(models, green_apples)

    plt.xlabel("Model ID", fontsize=12)
    plt.ylabel("Green Apples", fontsize=12)
    plt.title("Green Apples eaten per Model", fontsize=14)
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
    plot_green_apples(model_stats)
    plot_red_apples(model_stats)