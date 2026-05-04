# app.py
import yaml

def load_config(user_input):
    return yaml.safe_load(user_input) 
