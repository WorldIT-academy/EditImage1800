import os 
import json

def read_json(name_json: str):
    patch_file = os.path.abspath(__file__ + f"/../../../static/json/{name_json}")
    with open(patch_file, 'r') as file:
        return json.load(file)