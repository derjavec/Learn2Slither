action_id = {
    'UP' : 0,
    'RIGHT' : 1,
    'DOWN' : 2,
    'LEFT' : 3
}

def update_q_table(q_table, state, action, reward, next_state, alpha=0.1, gamma=0.9):

    if state not in q_table:
        q_table[state] = [0,0,0,0]

    if next_state not in q_table:
        q_table[next_state] = [0,0,0,0]

    idx = action_id[action]

    q_old = q_table[state][idx]
    q_max_next = max(q_table[next_state])

    q_new = q_old + alpha * (reward + gamma * q_max_next - q_old)

    q_table[state][idx] = q_new
    return q_table
