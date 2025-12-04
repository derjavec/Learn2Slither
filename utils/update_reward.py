def penalize_repeted_states(board, state):
    if board.visited_states[state] > board.size * 2:
        reward = board.reward - 10
    else:
        reward = board.reward
    return reward

