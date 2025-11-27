import random

directions = ['UP', 'RIGHT', 'DOWN', 'LEFT']

def direction_to_action(snake_dir, decision):
    if snake_dir is None:
        action = random.choice(directions)
    else:
        idx = directions.index(snake_dir)
        if decision == 'forward':
            action = directions[idx]
        elif decision == 'backward':
            action = directions[(idx + 2) % 4]
        elif decision == 'right':
            action = directions[(idx + 1) % 4]
        elif decision == 'left':
            action = directions[(idx + 3) % 4]
    return action



