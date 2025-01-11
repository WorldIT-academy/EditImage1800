import os
from os.path import abspath , join

import colorama

colorama.init()

GREEN = colorama.Fore.GREEN
YELLOW = colorama.Fore.YELLOW
RED = colorama.Fore.RED
RESET_STYLE = colorama.Style.RESET_ALL

def create_folder_media():
    try:
        # creating path to media folder 
        # ".." this command let move from file to folder or from folder to folder in reversal order 
        # __file__ point start for creating abspath
        path_media_folder = abspath(join(__file__, "..", "..", "..", "media"))
        for path in ['downloads', 'edits']:
            os.makedirs(join(path_media_folder, 'images', path), exist_ok= True)
            if not os.path.exists(join(path_media_folder, 'images', path)):
                print(f"{GREEN}Creating folder {YELLOW}{path}{RESET_STYLE}")
    except Exception as e:
        print(f"{RED}Error: {str(e)}{RESET_STYLE}")

