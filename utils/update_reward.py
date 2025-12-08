def penalize_repeated_states(board, state):
    """
    Apply a penalty if the snake revisits a state too often.
    """
    if board.visited_states.get(state, 0) > board.size * 2:
        return board.reward - 10
    return board.reward
