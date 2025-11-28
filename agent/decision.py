import random


action_id = ['UP','RIGHT','DOWN','LEFT']
options = ['forward', 'right', 'backward', 'left']


def take_decision(q_table, state, eps, snake_dir):
    if random.random() < eps:
        d = options[random.randint(0, 3)]
    else:
        q_max_idx = q_table.index(max(q_table))
        snake_dir_idx = action_id[snake_dir]
        idx = snake_dir_idx - q_max_idx
        d = options[idx]
    return d
