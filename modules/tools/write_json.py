"""
    use for rewrite information in json
"""

import os
import json

def rewrite_json(dict: dict, name_json: str):
    """ 
        find path to json and write new value
    """
    path_to_file = os.path.abspath(os.path.join(__file__, "..", "..", "..", "static", "json", name_json))
    with open(path_to_file, "w") as data_json:
        json.dump(obj = dict, fp = data_json, indent= 4)