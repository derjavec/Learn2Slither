"""
Decision module for the Snake RL agent.

This file provides the action-selection logic both for training
(epsilon-greedy) and for inference (exploitation with safeguards).
"""

import random
from typing import Dict, List, Tuple

ACTIONS = ["forward", "right", "left"]


def take_decision(
    q_table: Dict[Tuple, List[float]],
    state: Tuple,
    snake_dir: str,
    size: int
) -> str:
    """
    Select an action based on the Q-table for inference mode.
    """
    if state not in q_table:
        return random.choice(ACTIONS)

    q_values = q_table[state]
    q_min = min(q_values)
    q_max = max(q_values)
    diff = q_max - q_min

    if (diff < size * 3 and q_min > 0):
        idx = random.randint(0, 2)
    else:
        idx = q_values.index(q_max)

    return ACTIONS[idx]


def take_decision_training(
    q_table: Dict[Tuple, List[float]],
    state: Tuple,
    eps: float,
    snake_dir: str
) -> str:
    """
    Epsilon-greedy action selection for training.
    """
    explore = state not in q_table or random.random() < eps

    if explore:
        return random.choice(ACTIONS)

    q_values = q_table[state]
    q_max = max(q_values)
    idx = q_values.index(q_max)

    return ACTIONS[idx]
