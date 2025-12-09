"""
Convert a relative decision ('forward', 'right', 'left', 'backward')
into an absolute board action ('UP', 'RIGHT', 'DOWN', 'LEFT').
"""

directions = ['UP', 'RIGHT', 'DOWN', 'LEFT']

decision_offset = {
    'forward': 0,
    'right': 1,
    'backward': 2,
    'left': 3
}


def direction_to_action(snake_dir, decision):
    """
    Translate a relative snake decision into an absolute action.
    """
    if snake_dir not in directions:
        raise ValueError(f"Invalid snake_dir: {snake_dir}")

    if decision not in decision_offset:
        raise ValueError(f"Invalid decision: {decision}")

    idx = directions.index(snake_dir)
    offset = decision_offset[decision]
    return directions[(idx + offset) % 4]
