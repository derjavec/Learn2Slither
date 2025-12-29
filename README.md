# Learn2Slither

Learn2Slither is an educational reinforcement learning project that implements a classic **Snake** game environment and trains an agent to play it using **Q-learning**. The goal is not to build a perfect Snake AI, but to **understand, implement, and analyze the full RL loop from scratch**: environment design, state representation, reward shaping, training, evaluation, and visualization.

This project is intentionally explicit and low-level. There are no high-level RL libraries (like Stable-Baselines). Everything important is implemented manually so the learning process is transparent.

---

## Project Goals

* Build a fully controlled Snake environment
* Train an agent using tabular Q-learning
* Experiment with different hyperparameters and environment configurations
* Analyze learning behavior through logs and plots
* Keep the code simple, readable, and hackable

If you are looking for performance or deep learning, this is not the project. If you want to **actually understand reinforcement learning**, it is.

---

## Core Concepts Implemented

* Discrete grid-based environment
* Deterministic game mechanics
* Explicit state encoding
* Action-value function (Q-table)
* Epsilon-greedy exploration
* Learning rate (alpha) and discount factor (gamma)
* Episodic training loop
* Batch averaging for meaningful metrics

---

## Environment Overview

* The game runs on an **N x N grid**
* The snake:

  * Has a head and a growing body
  * Dies if it hits a wall or itself
* Apples:

  * **Green apples**: reward (+), increase snake length
  * **Red apples**: penalty (-), optional depending on config

All parameters (grid size, number of apples, rewards, etc.) are configurable.

---

## State Representation

The state is intentionally **hand-crafted and discrete**, not raw pixels.

Typical state information includes:

* Relative position of food
* Immediate obstacles (wall or body) in each direction
* Current movement direction

This keeps the Q-table finite and interpretable.

---

## Action Space

The agent can choose among **four discrete actions**:

* UP
* DOWN
* LEFT
* RIGHT

Invalid moves (like reversing into itself) are handled by the environment.

---

## Learning Algorithm

The agent uses **tabular Q-learning**:

Q(s, a) ← Q(s, a) + α [ r + γ max(Q(s', ·)) − Q(s, a) ]

Where:

* α (alpha): learning rate
* γ (gamma): discount factor
* r: reward from the environment
* s → s': state transition

Exploration is handled with an **epsilon-greedy strategy**.

---

## Training Loop

Each episode:

1. Reset the environment
2. Observe the initial state
3. Repeat until terminal state:

   * Choose action (exploration vs exploitation)
   * Apply action
   * Receive reward
   * Update Q-table
4. Store episode metrics

Training typically runs for **thousands of episodes**.

---

## Metrics & Visualization

Raw per-episode plots are noisy and misleading, so the project focuses on:

* **Batch averages** (e.g. every N episodes)
* Metrics such as:

  * Average snake length
  * Average steps survived
  * Average reward

This makes learning trends actually visible.

---

## Configuration System

Training is driven by configuration dictionaries / files, including:

* Number of episodes
* Batch size
* Grid size
* Learning rate (alpha)
* Discount factor (gamma)
* Epsilon value
* Number of green/red apples

Multiple configurations can be tested and compared.

---

## Code Quality

* Linted with **flake8 / pylint**
* Clear class separation (Environment, Agent, Trainer, Utils)
* No hidden magic
* No unnecessary abstractions

The code favors **clarity over cleverness**.

---

## Who This Project Is For

* Developers learning reinforcement learning fundamentals
* People who want to understand Q-learning deeply
* Students who don’t want black-box RL libraries

## Who It Is NOT For

* People looking for SOTA performance
* Deep learning / neural network enthusiasts
* Production-grade AI systems

---

## Possible Extensions

* Replace Q-table with a neural network (DQN)
* Add partial observability
* Change reward shaping
* Increase state complexity
* Add curriculum learning

---

## Summary

Learn2Slither is a **learning-first** reinforcement learning project.

It is simple on purpose, explicit on purpose, and imperfect on purpose.

If you understand this project, you understand the foundations of reinforcement learning.

That’s the point.
