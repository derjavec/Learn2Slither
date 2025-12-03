import random

action = ['forward', 'right', 'left']

def take_decision(q_table, state, eps, snake_dir):
    if state not in q_table or random.random() < eps:
        d = action[random.randint(0, 2)]
        # print('elige por azar:', d)
    else:
        # diff = max(q_table[state]) - min(q_table[state])
        # if diff < 20 and min(q_table[state]) > 0:
        #     q_max_idx = random.randint(0, 2)
        # else:
        q_max = max(q_table[state])
        q_max_idx = q_table[state].index(q_max)
        d = action[q_max_idx]
    # print(f'elige del estado:{state}, y tabla {q_table[state]} la opcion {d}')
    return d
