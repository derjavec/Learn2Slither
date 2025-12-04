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


def add_to_history(config, q_table):
    
    history = {
        'id' : 0,
        'config' : config,
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

def deserialize_keys(d):
    """Convierte claves string que representan tuplas en tuplas reales."""
    out = {}
    for k, v in d.items():
        if isinstance(k, str) and k.startswith("(") and k.endswith(")"):
            try:
                key = eval(k)
            except:
                key = k
        else:
            key = k

        if isinstance(v, dict):
            out[key] = deserialize_keys(v)
        else:
            out[key] = v

    return out


def load_models(model_id=None):
    path = "generated_files/history.json"
    if not os.path.exists(path):
        raise ValueError("No history.json found")

    with open(path, "r", encoding="utf-8") as f:
        all_histories = json.load(f)

    result = []

    for item in all_histories:
        idx = item["id"]
        cfg = item["config"]
        qtab = deserialize_keys(item["q_table"])

        if model_id is not None:
            if item.get("id") == model_id:
                result.append({"id":idx, "config": cfg, "q_table": qtab})
                return result
        else:
            result.append({"id":idx, "config": cfg, "q_table": qtab})

    if model_id is not None and not result:
        raise ValueError(f"Model ID {model_id} not found")

    return result


def rewrite_history_with_updates(updated_models, add_n):
    path = "generated_files/history.json"
    with open(path, "r", encoding="utf-8") as f:
        all_histories = json.load(f)

    updated_by_id = {m["id"]: m for m in updated_models}

    final = []
    for item in all_histories:
        model_id = item["id"]

        if model_id in updated_by_id:
            new_m = updated_by_id[model_id]
            episodes = new_m["config"]["episodes"] + add_n
            new_m["config"]["episodes"] = episodes
            final.append({
                "id": model_id,
                "config": new_m["config"],
                "q_table": serialize_keys(new_m["q_table"])
            })
        else:
            final.append(item)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(final, f, indent=2)
