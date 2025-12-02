action_id = {
    'forward' : 0,
    'right' : 1,
    'left' : 2
}

def update_q_table(q_table, state, action, reward, next_state, alpha=0.1, gamma=0.9):
    if state is None:
        return q_table
    if state not in q_table:
        q_table[state] = [0,0,0]

    if next_state is not None and next_state not in q_table:
        q_table[next_state] = [0,0,0]

    idx = action_id[action]

    q_old = q_table[state][idx]
    if next_state is None:
        q_max_next = 0
    else:
        q_max_next = max(q_table[next_state])

    q_new = q_old + alpha * (reward + gamma * q_max_next - q_old)

    q_table[state][idx] = q_new
    return q_table
