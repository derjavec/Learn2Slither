import argparse
import json
import os
import ast
import numpy as np

DEFAULT_CONFIG = {
    "episodes": 10000,
    "batch_size": 100,
    "e_greedy": 0.5,
    "alpha": 0.1,
    "gamma": 0.9,
    "size": 10,
    "green_apples": 2,
    "red_apples": 1,
}


def read_config_file(file_path: str) -> dict:
    """
    Read a configuration file in JSON or TXT format.
    """
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".json":
        with open(file_path) as f:
            return json.load(f)

    if ext == ".txt":
        config = {}
        with open(file_path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                key, value = line.split("=")
                key = key.strip()
                value = value.strip()
                try:
                    config[key] = ast.literal_eval(value)
                except Exception:
                    config[key] = value
        return config

    raise ValueError("Unknown file format. Please use .json or .txt")


def replace_dict_values(base: dict, new: dict) -> dict:
    """
    Replace values in a base dictionary with values from a new dictionary.
    """
    for k, v in new.items():
        if v is not None:
            base[k] = v
    return base


def check_config(config: dict):
    """
    Validate Q-learning configuration.
    """
    required_keys = ["episodes", "batch_size", "e_greedy", "alpha", "gamma", "size", "green_apples", "red_apples"]
    apples = ["green_apples", "red_apples"]
    coef = ["alpha", "gamma", "e_greedy"]
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Configuration Error: missing key '{key}'")
        if isinstance(config[key], (int, float)) and config[key] < 0:
            raise ValueError(f"Configuration Error: '{key}' must be non-negative")
        if config['size'] < 5:
            raise ValueError(f"Configuration Error: board size must be greater than 5")
        for app in apples:
            if config[app] < 1:
                raise ValueError(f"Configuration Error: {app} must be greater than 1")
        for c in coef:
            if config[c] > 1:
                raise ValueError(f"Configuration Error: {c} must be between 0 and 1")


def get_config() -> dict:
    """
    Load and parse the configuration from defaults, command-line arguments,
    or a file.
    """
    config = DEFAULT_CONFIG.copy()

    parser = argparse.ArgumentParser(description="Train a Q-learning Snake agent")

    parser.add_argument("--episodes", type=int, help="Number of episodes")
    parser.add_argument("--batch_size", type=int, help="Batch size")
    parser.add_argument("--e_greedy", type=float, help="Epsilon greedy probability")
    parser.add_argument("--alpha", type=float, help="Learning rate")
    parser.add_argument("--gamma", type=float, help="Discount factor")
    parser.add_argument("--size", type=int, help="Board size")
    parser.add_argument("--green_apples", type=int, help="Number of green apples")
    parser.add_argument("--red_apples", type=int, help="Number of red apples")
    parser.add_argument("--config_file", type=str,nargs = '?', help="Path to JSON or TXT config file")

    args = parser.parse_args()
    args_dict = vars(args)

    if args_dict.get("config_file"):
        config_dict = read_config_file(args_dict.pop("config_file"))
        config = replace_dict_values(config, config_dict)

    config = replace_dict_values(config, args_dict)

    check_config(config)

    return config

