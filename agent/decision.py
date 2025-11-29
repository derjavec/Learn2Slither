import random

action = ['forward', 'right', 'backward', 'left']

def take_decision(q_table, state, eps, snake_dir):
    if state not in q_table or random.random() < eps:
        d = action[random.randint(0, 3)]
    else:
        q_max = max(q_table[state])
        q_max_idx = q_table[state].index(q_max)
        d = action[q_max_idx]
    return d
