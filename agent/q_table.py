"""
Q-table update logic for the Snake RL agent.

Implements the standard Q-learning update rule:
    Q(s, a) ← Q(s, a) + α * (r + γ * max_a' Q(s', a') − Q(s, a))
"""

from typing import Dict, List, Tuple

ACTION_ID = {
    "forward": 0,
    "right": 1,
    "left": 2,
}


def update_q_table(
    q_table: Dict[Tuple, List[float]],
    state: Tuple,
    action: str,
    reward: float,
    next_state: Tuple | None,
    alpha: float = 0.1,
    gamma: float = 0.9,
) -> Dict[Tuple, List[float]]:
    """
    Update the Q-table according to the Q-learning rule.
    """
    if state is None:
        return q_table

    if state not in q_table:
        q_table[state] = [0.0, 0.0, 0.0]

    if next_state is not None and next_state not in q_table:
        q_table[next_state] = [0.0, 0.0, 0.0]

    idx = ACTION_ID[action]
    q_old = q_table[state][idx]

    if next_state is None:
        q_max_next = 0.0
    else:
        q_max_next = max(q_table[next_state])

    q_new = q_old + alpha * (reward + gamma * q_max_next - q_old)
    q_table[state][idx] = q_new

    return q_table
