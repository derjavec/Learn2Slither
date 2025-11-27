import random

options = ['forward', 'backward', 'right', 'left']
def take_random_decision(state):
    decision = random.choice(options)
    return decision