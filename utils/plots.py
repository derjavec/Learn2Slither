import matplotlib.pyplot as plt

def avg_per_batch(batch_size, x):
    avg = []
    batch_i = []
    for i in range(0, len(x), batch_size):
        batch = x[i : i + batch_size]
        avg.append(sum(batch)/len(batch))
        batch_i.append(i)
    return avg, batch_i
        



def plot_snake_length(model_history, batch_size):


    episodes = sorted(model_history.keys())

    snake_lens = [model_history[e]['snake_len'] for e in episodes]
    snake_avg, batch = avg_per_batch(batch_size, snake_lens)
    plt.figure(figsize=(10, 6))
    plt.plot(batch, snake_avg)
    plt.xlabel("Episodes", fontsize=12)
    plt.title("Snake Length", fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.show()


def plot_movements(model_history, batch_size):

    episodes = sorted(model_history.keys())
    movements = [model_history[e]['movements'] for e in episodes]
    movements_avg, batch = avg_per_batch(batch_size, movements)
    plt.figure(figsize=(10, 6))
    plt.plot(batch, movements_avg)
    plt.xlabel("Episodes", fontsize=12)
    plt.title("Movements", fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.show()

def plot_q_table_length(model_history):

    episodes = sorted(model_history.keys())
    q_table_lens = [model_history[e]['q_table_len'] for e in episodes]
    plt.figure(figsize=(10, 6))
    plt.plot(episodes, q_table_lens)
    plt.xlabel("Episodes", fontsize=12)
    plt.title("Q_Table Length", fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.show()

def plot_model_history(model_history, batch_size):
    plot_snake_length(model_history, batch_size)
    plot_movements(model_history, batch_size)
    plot_q_table_length(model_history)