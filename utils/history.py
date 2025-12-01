def add_to_history(config, q_table, model_history):
    if history is None:
        history = {
            'id' : 0,
            'config' : config,
            'model_history' : model_history,
            'q_table' : q_table
        }