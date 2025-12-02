import os
import json

def same_config(config1,config2) -> bool:
    """
    Compare two model configurations.

    Only compares selected relevant keys.
    """
    keys_to_compare = [
        "episodes",
        "batch_size",
        "alpha",
        "gamma",
        "size",
        "green_apples",
        "red_apples"
    ]

    for key in keys_to_compare:
        if config1.get(key) != config2.get(key):
            return False
    return True

def serialize_keys(d):
    return {str(k): v for k, v in d.items()}


def add_to_history(config, q_table, model_history):
    
    history = {
        'id' : 0,
        'config' : config,
        'model_history' : model_history,
        'q_table': serialize_keys(q_table)
    }

    output_folder = 'generated_files'
    filename = 'history.json'
    os.makedirs(output_folder, exist_ok=True)
    path = os.path.join(output_folder, filename)
    if not os.path.exists(path):
        history["id"] = 0
        with open(path, "w", encoding="utf-8") as f:
            json.dump([history], f, indent=4)
        return

    with open(path, "r", encoding="utf-8") as f:
        all_histories = json.load(f)

    for item in all_histories:
        if "config" in item and same_config(item["config"], config):
            return 

    existing_ids = [h.get("id", -1) for h in all_histories]
    new_id = max(existing_ids) + 1 if existing_ids else 0
    history["id"] = new_id
    all_histories.append(history)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(all_histories, f, indent=4)

    return 