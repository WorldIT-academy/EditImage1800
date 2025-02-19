"""
    ### Function to find the absolute path of a given path.
    it gives the absolute path of the path relative to the main.py file directory

    example usage:
    ```python
        print(search_path("static/json/config.json"))
        #Output "/path to main.py/static/json/config.json"
    ```

    © Mykytenko Petro, All rights reserved.
"""
import sys, os

def search_path(path : str) -> str:
    if getattr(sys, 'frozen', False):
        path = os.path.abspath(os.path.join(".", "_internal", *path.split("/")))
    else:
        path = os.path.abspath(os.path.join(".", *path.split("/")))

    return path